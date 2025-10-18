use actix_web::{dev::ServiceRequest, Error};
use actix_web_httpauth::extractors::bearer::BearerAuth;
use crate::config::AppConfig;
use crate::utils::jwt::JwtUtil;

pub async fn validator(
    mut req: ServiceRequest,
    credentials: BearerAuth,
) -> Result<ServiceRequest, (Error, ServiceRequest)> {
    let token = credentials.token();

    let config = req
        .app_data::<AppConfig>()
        .ok_or_else(|| (actix_web::error::ErrorInternalServerError("AppConfig missing"), req))?;

    match JwtUtil::decode_access_token(token, config) {
        Ok(token_data) => {
            // Wrap user ID in Arc so ReqData can extract it
            req.extensions_mut().insert(token_data.claims.sub);
            Ok(req)
        }
        Err(_) => Err((actix_web::error::ErrorUnauthorized("Invalid token"), req)),
    }
}
