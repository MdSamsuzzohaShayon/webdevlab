mod config;
mod db;

use actix_web::{App, HttpServer};

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let config = config::AppConfig::from_env();

    // Connect to PostgreSQL
    let pg_pool = db::postgres::init_db(&config.database_url).await;

    // Connect to Redis
    let redis_client = db::redis::init_client(&config.redis_url)
        .expect("❌ Failed to connect to Redis");

    println!("🚀 Server running at http://127.0.0.1:{}", config.port);

    HttpServer::new(move || {
        App::new()
            .app_data(pg_pool.clone())
            .app_data(redis_client.clone())
    })
    .bind(("127.0.0.1", config.port))?
    .run()
    .await
}
