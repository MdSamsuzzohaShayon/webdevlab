use dotenvy::dotenv;
use std::env;


pub struct AppConfig{
    pub database_url: String,
    pub redis_url: String,
    pub port: u16,
}

impl AppConfig{
    pub fn from_env() -> Self{
        dotenv().ok();

        Self{
            database_url: env::var("DATABASE_URL").expect("DATABASE_URL missing"),
            redis_url: env::var("REDIS_URL").unwrap_or("redis://127.0.0.1/".into()),
            port: env::var("PORT").unwrap_or("8000".into()).parse().unwrap(),
        }
    }
}