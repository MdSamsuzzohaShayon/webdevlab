use actix_web::{web, HttpResponse, post, get};
use validator::Validate;
use crate::{
    models::user::{RegisterUser, LoginUser, ForgotPassword, ResetPassword, VerifyEmail},
    services::auth_service::AuthService,
    errors::AppError,
};

#[post("/register")]
async fn register(
    auth_service: web::Data<AuthService>,
    user_data: web::Json<RegisterUser>,
) -> Result<HttpResponse, AppError> {
    user_data.validate().map_err(|e| AppError::ValidationError(e.to_string()))?;
    
    auth_service.register(user_data.into_inner()).await?;
    
    Ok(HttpResponse::Created().json(serde_json::json!({
        "message": "User registered successfully. Please check your email for verification."
    })))
}

#[post("/login")]
async fn login(
    auth_service: web::Data<AuthService>,
    login_data: web::Json<LoginUser>,
) -> Result<HttpResponse, AppError> {
    login_data.validate().map_err(|e| AppError::ValidationError(e.to_string()))?;
    
    let response = auth_service.login(login_data.into_inner()).await?;
    
    Ok(HttpResponse::Ok().json(response))
}

#[post("/refresh")]
async fn refresh_token(
    auth_service: web::Data<AuthService>,
    token: web::Json<serde_json::Value>,
) -> Result<HttpResponse, AppError> {
    let refresh_token = token.get("refresh_token")
        .and_then(|v| v.as_str())
        .ok_or_else(|| AppError::ValidationError("Refresh token is required".to_string()))?;
    
    let response = auth_service.refresh_token(refresh_token).await?;
    
    Ok(HttpResponse::Ok().json(response))
}

#[post("/logout")]
async fn logout(
    auth_service: web::Data<AuthService>,
    user_id: web::ReqData<i32>,
) -> Result<HttpResponse, AppError> {
    auth_service.logout(*user_id).await?;
    
    Ok(HttpResponse::Ok().json(serde_json::json!({
        "message": "Logged out successfully"
    })))
}

#[post("/verify-email")]
async fn verify_email(
    auth_service: web::Data<AuthService>,
    data: web::Json<VerifyEmail>,
) -> Result<HttpResponse, AppError> {
    auth_service.verify_email(data.token.clone()).await?;
    
    Ok(HttpResponse::Ok().json(serde_json::json!({
        "message": "Email verified successfully"
    })))
}

#[post("/forgot-password")]
async fn forgot_password(
    auth_service: web::Data<AuthService>,
    data: web::Json<ForgotPassword>,
) -> Result<HttpResponse, AppError> {
    auth_service.forgot_password(data.email.clone()).await?;
    
    Ok(HttpResponse::Ok().json(serde_json::json!({
        "message": "Password reset instructions sent to your email"
    })))
}

#[post("/reset-password")]
async fn reset_password(
    auth_service: web::Data<AuthService>,
    data: web::Json<ResetPassword>,
) -> Result<HttpResponse, AppError> {
    data.validate().map_err(|e| AppError::ValidationError(e.to_string()))?;
    
    auth_service.reset_password(data.into_inner()).await?;
    
    Ok(HttpResponse::Ok().json(serde_json::json!({
        "message": "Password reset successfully"
    })))
}

#[get("/me")]
async fn get_me(
    auth_service: web::Data<AuthService>,
    user_id: web::ReqData<i32>,
) -> Result<HttpResponse, AppError> {
    let user = auth_service.get_user_by_id(*user_id).await?;
    
    Ok(HttpResponse::Ok().json(user))
}

pub fn init_routes(cfg: &mut web::ServiceConfig) {
    cfg.service(register)
        .service(login)
        .service(refresh_token)
        .service(logout)
        .service(verify_email)
        .service(forgot_password)
        .service(reset_password)
        .service(get_me);
}


pub fn init_protected_routes(cfg: &mut web::ServiceConfig) {
    cfg.service(get_me); // only authenticated routes
}