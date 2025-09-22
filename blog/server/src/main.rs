mod config;
mod db;
mod errors;
mod api;
mod models;
mod services;
mod utils;

use actix_web::{App, HttpServer, web};
use actix_web_httpauth::middleware::HttpAuthentication;
use sqlx::migrate::Migrator;
use std::path::Path;
use crate::{
    config::AppConfig,
    services::{auth_service::AuthService, cache_service::CacheService},
    utils::middleware::validator,
};

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let config = AppConfig::from_env();

    // Connect to PostgreSQL
    let pg_pool = db::postgres::init_db(&config.database_url)
        .await
        .expect("❌ Failed to connect to PostgreSQL");

    // Run migrations
    run_migrations(&pg_pool).await;

    // Connect to Redis
    let redis_client = db::redis::init_client(&config.redis_url)
        .expect("❌ Failed to connect to Redis");

    // Create services
    let cache_service = CacheService::new(redis_client.clone());
    let auth_service = AuthService::new(pg_pool.clone(), cache_service, config.clone());

    println!("🚀 Server running at http://127.0.0.1:{}", config.port);

    HttpServer::new(move || {
        let auth_middleware = HttpAuthentication::bearer(validator);

        App::new()
            .app_data(web::Data::new(pg_pool.clone()))
            .app_data(web::Data::new(redis_client.clone()))
            .app_data(web::Data::new(auth_service.clone()))
            .app_data(web::Data::new(config.clone()))
            .service(
                web::scope("/api/auth")
                    .configure(api::auth::init_routes)
            )
            .service(
                web::scope("/api/protected")
                    .wrap(auth_middleware)
                    .configure(api::auth::init_protected_routes)
            )
    })
    .bind(("127.0.0.1", config.port))?
    .run()
    .await
}

async fn run_migrations(pool: &sqlx::PgPool) {
    let migrator = Migrator::new(Path::new("./migrations"))
        .await
        .expect("❌ Failed to load migrations");
    
    migrator.run(pool)
        .await
        .expect("❌ Failed to run migrations");
    
    println!("✅ Database migrations completed");
}