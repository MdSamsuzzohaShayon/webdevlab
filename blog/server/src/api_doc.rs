use utoipa::OpenApi;
use crate::api::auth;

#[derive(OpenApi)]
#[openapi(
    paths(
        auth::register,
        auth::login,
        auth::refresh_token,
        auth::logout,
        auth::verify_email,
        auth::forgot_password,
        auth::reset_password,
        auth::get_me
    ),
    components(
        schemas(
            crate::models::user::RegisterUser,
            crate::models::user::LoginUser,
            crate::models::user::AuthResponse,
            crate::models::user::UserResponse
        )
    ),
    tags(
        (name = "Auth", description = "Authentication related endpoints")
    )
)]
pub struct ApiDoc;
