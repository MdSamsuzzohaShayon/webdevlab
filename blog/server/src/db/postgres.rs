use sqlx::{PgPool, postgres::PgPoolOptions};

pub async fn init_db(database_url: &str) -> PgPool {
    // Create a connection pool with proper configuration
    let pool = PgPoolOptions::new()
        .max_connections(5)
        .connect(database_url)
        .await
        .expect("❌ Failed to connect to PostgreSQL");
    
    println!("✅ Connected to PostgreSQL");
    pool
}