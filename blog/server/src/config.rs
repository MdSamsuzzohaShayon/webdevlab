use dotenvy::dotenv;
use std::env;

#[derive(Debug, Clone)]
pub struct AppConfig {
    pub database_url: String,
    pub redis_url: String,
    pub port: u16,
    pub jwt_secret: String,
    pub jwt_expires_in: i64,
    pub refresh_token_expires_in: i64,
    pub smtp_host: String,
    pub smtp_port: u16,
    pub smtp_username: String,
    pub smtp_password: String,
    pub from_email: String,
    pub frontend_url: String,
}

impl AppConfig {
    pub fn from_env() -> Self {
        dotenv().ok();

        AppConfig {
            database_url: env::var("DATABASE_URL").expect("DATABASE_URL must be set"),
            redis_url: env::var("REDIS_URL").expect("REDIS_URL must be set"),
            port: env::var("PORT")
                .unwrap_or_else(|_| "8000".to_string())
                .parse()
                .expect("PORT must be a number"),
            jwt_secret: env::var("JWT_SECRET").expect("JWT_SECRET must be set"),
            jwt_expires_in: env::var("JWT_EXPIRES_IN")
                .unwrap_or_else(|_| "3600".to_string())
                .parse()
                .expect("JWT_EXPIRES_IN must be a number"),
            refresh_token_expires_in: env::var("REFRESH_TOKEN_EXPIRES_IN")
                .unwrap_or_else(|_| "2592000".to_string())
                .parse()
                .expect("REFRESH_TOKEN_EXPIRES_IN must be a number"),
            smtp_host: env::var("SMTP_HOST").expect("SMTP_HOST must be set"),
            smtp_port: env::var("SMTP_PORT")
                .unwrap_or_else(|_| "587".to_string())
                .parse()
                .expect("SMTP_PORT must be a number"),
            smtp_username: env::var("SMTP_USERNAME").expect("SMTP_USERNAME must be set"),
            smtp_password: env::var("SMTP_PASSWORD").expect("SMTP_PASSWORD must be set"),
            from_email: env::var("FROM_EMAIL").expect("FROM_EMAIL must be set"),
            frontend_url: env::var("FRONTEND_URL").expect("FRONTEND_URL must be set"),
        }
    }
}
