mod api;
mod api_doc; // add this at the top
mod config;
mod db;
mod errors;
mod models;
mod services;
mod utils;

use crate::api_doc::ApiDoc;
use crate::{
    config::AppConfig,
    services::{auth_service::AuthService, cache_service::CacheService},
    utils::middleware::validator,
};
use actix_web::{App, HttpResponse, HttpServer, Responder, web};
use actix_web_httpauth::middleware::HttpAuthentication;
use sqlx::migrate::Migrator;
use std::path::Path;
use utoipa::OpenApi;
use utoipa_swagger_ui::SwaggerUi;

use crate::services::{category_service::CategoryService, post_service::PostService};

// A simple test handler
async fn test_route() -> impl Responder {
    HttpResponse::Ok().body("Test route is working!")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let config = AppConfig::from_env();

    // Connect to PostgreSQL
    let pg_pool = db::postgres::init_db(&config.database_url).await?; // assuming init_db returns Result<PgPool, _>

    // Connect to Redis
    let redis_client =
        db::redis::init_client(&config.redis_url).expect("❌ Failed to connect to Redis");

    // Create services
    let cache_service = CacheService::new(redis_client.clone());
    let auth_service = AuthService::new(pg_pool.clone(), cache_service, config.clone());
    let post_service = PostService::new(pg_pool.clone());
    let category_service = CategoryService::new(pg_pool.clone());

    println!("🚀 Server running at http://127.0.0.1:{}", config.port);

    // Clone config for the closure so the original can still be used in .bind()
    let server_config = config.clone();

    HttpServer::new(move || {
        // Create separate middleware instances for each scope
        let posts_auth_middleware = HttpAuthentication::bearer(validator);
        let categories_auth_middleware = HttpAuthentication::bearer(validator);
        let protected_auth_middleware = HttpAuthentication::bearer(validator);

        App::new()
            .app_data(web::Data::new(pg_pool.clone()))
            .app_data(web::Data::new(redis_client.clone()))
            .app_data(web::Data::new(auth_service.clone()))
            .app_data(web::Data::new(post_service.clone()))
            .app_data(web::Data::new(category_service.clone()))
            .app_data(web::Data::new(server_config.clone())) // use cloned config here
            // Public auth routes (all except /me)
            .service(web::scope("/api/auth").configure(api::auth::init_routes))
            .service(
                web::scope("/api/posts")
                    // .wrap(posts_auth_middleware.clone())
                    .configure(api::posts::init_routes),
            )
            .service(
                web::scope("/api/categories")
                    // .wrap(categories_auth_middleware)
                    .configure(api::categories::init_routes),
            )
            // Protected routes - only /api/auth/me
            .service(
                web::scope("/api/auth")
                    .wrap(protected_auth_middleware)
                    .configure(api::auth::init_protected_routes), // This only has /me
            )
            .route("/api/test", web::get().to(test_route))
            // Swagger UI route
            .service(
                SwaggerUi::new("/api/docs/{_:.*}").url("/api-doc/openapi.json", ApiDoc::openapi()),
            )
    })
    .bind(("127.0.0.1", config.port))? // original config is still available here
    .run()
    .await
}
