use actix_web::{HttpResponse, ResponseError};
use serde::Serialize;
use std::fmt;

#[derive(Debug)]
pub enum AppError {
    DatabaseError(sqlx::Error),
    RedisError(redis::RedisError),
    JwtError(jsonwebtoken::errors::Error),
    BcryptError(bcrypt::BcryptError),
    EmailError(String),
    ValidationError(String),
    Unauthorized(String),
    NotFound(String),
    InternalError(String),
}

#[derive(Serialize)]
struct ErrorResponse {
    error: String,
    message: String,
}

impl fmt::Display for AppError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            AppError::DatabaseError(e) => write!(f, "Database error: {}", e),
            AppError::RedisError(e) => write!(f, "Redis error: {}", e),
            AppError::JwtError(e) => write!(f, "JWT error: {}", e),
            AppError::BcryptError(e) => write!(f, "Bcrypt error: {}", e),
            AppError::EmailError(e) => write!(f, "Email error: {}", e),
            AppError::ValidationError(e) => write!(f, "Validation error: {}", e),
            AppError::Unauthorized(e) => write!(f, "Unauthorized: {}", e),
            AppError::NotFound(e) => write!(f, "Not found: {}", e),
            AppError::InternalError(e) => write!(f, "Internal error: {}", e),
        }
    }
}

impl ResponseError for AppError {
    fn error_response(&self) -> HttpResponse {
        match self {
            AppError::Unauthorized(_) => HttpResponse::Unauthorized().json(ErrorResponse {
                error: "Unauthorized".to_string(),
                message: self.to_string(),
            }),
            AppError::ValidationError(_) => HttpResponse::BadRequest().json(ErrorResponse {
                error: "Validation Error".to_string(),
                message: self.to_string(),
            }),
            AppError::NotFound(_) => HttpResponse::NotFound().json(ErrorResponse {
                error: "Not Found".to_string(),
                message: self.to_string(),
            }),
            _ => HttpResponse::InternalServerError().json(ErrorResponse {
                error: "Internal Server Error".to_string(),
                message: self.to_string(),
            }),
        }
    }
}

// Implement From traits for error conversions
impl From<sqlx::Error> for AppError {
    fn from(err: sqlx::Error) -> Self {
        AppError::DatabaseError(err)
    }
}

impl From<redis::RedisError> for AppError {
    fn from(err: redis::RedisError) -> Self {
        AppError::RedisError(err)
    }
}

impl From<jsonwebtoken::errors::Error> for AppError {
    fn from(err: jsonwebtoken::errors::Error) -> Self {
        AppError::JwtError(err)
    }
}

impl From<bcrypt::BcryptError> for AppError {
    fn from(err: bcrypt::BcryptError) -> Self {
        AppError::BcryptError(err)
    }
}