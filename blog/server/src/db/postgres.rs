use sqlx::{PgPool, postgres::PgPoolOptions};
use std::io;

pub async fn init_db(database_url: &str) -> io::Result<PgPool> {
    let pool = PgPoolOptions::new()
        .max_connections(5)
        .connect(database_url)
        .await
        .map_err(|e| io::Error::new(io::ErrorKind::Other, e))?;

    println!("✅ Connected to PostgreSQL");
    Ok(pool)
}
