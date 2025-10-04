// src/utils/middleware.rs
use actix_web::{dev::ServiceRequest, Error};
use actix_web_httpauth::extractors::bearer::BearerAuth;

pub async fn validator(
    req: ServiceRequest,
    credentials: BearerAuth,
) -> Result<ServiceRequest, (Error, ServiceRequest)> {
    let token = credentials.token();

    // Temporary demo check — replace with your JwtUtil::verify_token
    if token == "valid_token" {
        Ok(req)
    } else {
        Err((actix_web::error::ErrorUnauthorized("Invalid token"), req))
    }
}
