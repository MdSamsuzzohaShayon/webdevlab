use sqlx::{PgPool, Pool, Postgres};

pub async fn init_db(database_url: &str) -> PgPool {
    // Create a connection pool
    let pool: Pool<Postgres> = PgPool::connect(database_url)
        .await
        .expect("❌ Failed to connect to PostgreSQL");
    println!("✅ Connected to PostgreSQL");
    pool
}
