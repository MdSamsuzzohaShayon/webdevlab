use crate::api::{auth, categories, posts};
use utoipa::OpenApi;

#[derive(OpenApi)]
#[openapi(
    paths(
        // Auth endpoints
        auth::register,
        auth::login,
        auth::refresh_token,
        auth::logout,
        auth::verify_email,
        auth::forgot_password,
        auth::reset_password,
        auth::get_me,
        // Posts endpoints
        posts::create_post,
        posts::get_all_posts,
        posts::get_post,
        posts::get_posts_by_author,
        posts::get_posts_by_category,
        posts::update_post,
        posts::delete_post,
        // Categories endpoints
        categories::create_category,
        categories::get_all_categories,
        categories::get_category,
        categories::get_category_by_slug,
        categories::update_category,
        categories::delete_category,
    ),
    components(
        schemas(
            // Auth schemas
            crate::models::user::RegisterUser,
            crate::models::user::LoginUser,
            crate::models::user::ForgotPassword,
            crate::models::user::ResetPassword,
            crate::models::user::VerifyEmail,
            crate::models::user::AuthResponse,
            crate::models::user::UserResponse,
            // Posts schemas
            crate::models::post::CreatePost,
            crate::models::post::UpdatePost,
            crate::models::post::PostResponse,
            // Categories schemas
            crate::models::category::CreateCategory,
            crate::models::category::UpdateCategory,
            crate::models::category::CategoryResponse,
        )
    ),
    tags(
        (name = "Auth", description = "Authentication related endpoints"),
        (name = "Posts", description = "Blog posts management endpoints"),
        (name = "Categories", description = "Categories management endpoints")
    )
)]
pub struct ApiDoc;
