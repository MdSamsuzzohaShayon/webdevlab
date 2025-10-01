use sqlx::PgPool;
use uuid::Uuid;
use chrono::Utc;
use crate::{
    models::user::{User, RegisterUser, LoginUser, ForgotPassword, ResetPassword, VerifyEmail, AuthResponse, UserResponse},
    utils::{jwt::JwtUtil, password::PasswordUtil, email::EmailUtil},
    services::cache_service::CacheService,
    config::AppConfig,
    errors::AppError,
};

#[derive(Clone)]
pub struct AuthService {
    pool: PgPool,
    cache_service: CacheService,
    config: AppConfig,
}

impl AuthService {
    pub fn new(pool: PgPool, cache_service: CacheService, config: AppConfig) -> Self {
        Self {
            pool,
            cache_service,
            config,
        }
    }

    pub async fn register(&self, user_data: RegisterUser) -> Result<(), AppError> {
        // Check if user already exists
        let existing_user = sqlx::query_as::<_, User>(
            "SELECT * FROM users WHERE email = $1"
        )
        .bind(&user_data.email)
        .fetch_optional(&self.pool)
        .await?;

        if existing_user.is_some() {
            return Err(AppError::ValidationError("User already exists".to_string()));
        }

        // Hash password
        let password_hash = PasswordUtil::hash_password(&user_data.password)?;

        // Generate verification token
        let verification_token = Uuid::new_v4().to_string();

        // Create user
        sqlx::query!(
            "INSERT INTO users (email, password_hash, first_name, last_name, photo, verification_token) 
             VALUES ($1, $2, $3, $4, $5, $6)",
            user_data.email,
            password_hash,
            user_data.first_name,
            user_data.last_name,
            None::<String>,   // photo is optional, set to NULL initially
            verification_token
        )
        .execute(&self.pool)
        .await?;

        // Store verification token in Redis
        self.cache_service.store_verification_token(
            &user_data.email,
            &verification_token,
            24 * 60 * 60, // 24 hours
        )?;

        // Send verification email
        EmailUtil::send_verification_email(
            &self.config,
            &user_data.email,
            &verification_token,
        ).await.map_err(|e| AppError::EmailError(e))?;

        Ok(())
    }

    pub async fn login(&self, login_data: LoginUser) -> Result<AuthResponse, AppError> {
        // Find user
        let user = sqlx::query_as::<_, User>(
            "SELECT * FROM users WHERE email = $1"
        )
        .bind(&login_data.email)
        .fetch_optional(&self.pool)
        .await?
        .ok_or_else(|| AppError::Unauthorized("Invalid credentials".to_string()))?;

        // Verify password
        if !PasswordUtil::verify_password(&login_data.password, &user.password_hash)? {
            return Err(AppError::Unauthorized("Invalid credentials".to_string()));
        }

        // Check if email is verified
        if !user.is_verified {
            return Err(AppError::Unauthorized("Email not verified".to_string()));
        }

        // Generate tokens
        let access_token = JwtUtil::generate_access_token(user.id, &self.config)?;
        let refresh_token = JwtUtil::generate_refresh_token(user.id, &self.config)?;

        // Store refresh token in Redis
        self.cache_service.store_refresh_token(
            user.id,
            &refresh_token,
            self.config.refresh_token_expires_in as u64,
        )?;

        Ok(AuthResponse {
            access_token,
            refresh_token,
            token_type: "Bearer".to_string(),
            expires_in: self.config.jwt_expires_in,
            user: UserResponse::from(user),
        })
    }

    pub async fn refresh_token(&self, refresh_token: &str) -> Result<AuthResponse, AppError> {
        // Verify refresh token
        let claims = JwtUtil::verify_token(refresh_token, &self.config)?;

        // Check if refresh token exists in Redis
        let stored_token = self.cache_service.get_refresh_token(claims.sub)?;
        
        if stored_token != refresh_token {
            return Err(AppError::Unauthorized("Invalid refresh token".to_string()));
        }

        // Generate new tokens
        let access_token = JwtUtil::generate_access_token(claims.sub, &self.config)?;
        let new_refresh_token = JwtUtil::generate_refresh_token(claims.sub, &self.config)?;

        // Update refresh token in Redis
        self.cache_service.store_refresh_token(
            claims.sub,
            &new_refresh_token,
            self.config.refresh_token_expires_in as u64,
        )?;

        // Get user data
        let user = sqlx::query_as::<_, User>(
            "SELECT * FROM users WHERE id = $1"
        )
        .bind(claims.sub)
        .fetch_one(&self.pool)
        .await?;

        Ok(AuthResponse {
            access_token,
            refresh_token: new_refresh_token,
            token_type: "Bearer".to_string(),
            expires_in: self.config.jwt_expires_in,
            user: UserResponse::from(user),
        })
    }

    pub async fn logout(&self, user_id: i32) -> Result<(), AppError> {
        // Delete refresh token from Redis
        self.cache_service.delete_refresh_token(user_id)?;
        Ok(())
    }

    pub async fn verify_email(&self, token: String) -> Result<(), AppError> {
        // Find user by verification token
        let user = sqlx::query_as::<_, User>(
            "SELECT * FROM users WHERE verification_token = $1"
        )
        .bind(&token)
        .fetch_optional(&self.pool)
        .await?
        .ok_or_else(|| AppError::NotFound("Invalid verification token".to_string()))?;

        // Verify token in Redis
        let stored_token = self.cache_service.get_verification_token(&user.email)?;
        
        if stored_token != token {
            return Err(AppError::ValidationError("Invalid verification token".to_string()));
        }

        // Update user as verified
        sqlx::query!(
            "UPDATE users SET is_verified = true, verification_token = NULL WHERE id = $1",
            user.id
        )
        .execute(&self.pool)
        .await?;

        Ok(())
    }

    pub async fn forgot_password(&self, email: String) -> Result<(), AppError> {
        // Find user
        let user = sqlx::query_as::<_, User>(
            "SELECT * FROM users WHERE email = $1"
        )
        .bind(&email)
        .fetch_optional(&self.pool)
        .await?
        .ok_or_else(|| AppError::NotFound("User not found".to_string()))?;

        // Generate reset token
        let reset_token = Uuid::new_v4().to_string();

        // Store reset token in database and Redis
        sqlx::query!(
            "UPDATE users SET reset_token = $1, reset_token_expires = $2 WHERE id = $3",
            reset_token,
            Utc::now() + chrono::Duration::hours(1),
            user.id
        )
        .execute(&self.pool)
        .await?;

        self.cache_service.store_reset_token(
            &email,
            &reset_token,
            60 * 60, // 1 hour
        )?;

        // Send reset email
        EmailUtil::send_password_reset_email(
            &self.config,
            &email,
            &reset_token,
        ).await.map_err(|e| AppError::EmailError(e))?;

        Ok(())
    }

    pub async fn reset_password(&self, reset_data: ResetPassword) -> Result<(), AppError> {
        // Find user by reset token
        let user = sqlx::query_as::<_, User>(
            "SELECT * FROM users WHERE reset_token = $1 AND reset_token_expires > $2"
        )
        .bind(&reset_data.token)
        .bind(Utc::now())
        .fetch_optional(&self.pool)
        .await?
        .ok_or_else(|| AppError::ValidationError("Invalid or expired reset token".to_string()))?;

        // Verify token in Redis
        let stored_token = self.cache_service.get_reset_token(&user.email)?;
        
        if stored_token != reset_data.token {
            return Err(AppError::ValidationError("Invalid reset token".to_string()));
        }

        // Hash new password
        let password_hash = PasswordUtil::hash_password(&reset_data.new_password)?;

        // Update password and clear reset token
        sqlx::query!(
            "UPDATE users SET password_hash = $1, reset_token = NULL, reset_token_expires = NULL WHERE id = $2",
            password_hash,
            user.id
        )
        .execute(&self.pool)
        .await?;

        // Delete reset token from Redis
        self.cache_service.delete_reset_token(&user.email)?;

        Ok(())
    }

    pub async fn get_user_by_id(&self, user_id: i32) -> Result<User, AppError> {
        let user = sqlx::query_as::<_, User>(
            "SELECT * FROM users WHERE id = $1"
        )
        .bind(user_id)
        .fetch_one(&self.pool)
        .await?;
        
        Ok(user)
    }
}