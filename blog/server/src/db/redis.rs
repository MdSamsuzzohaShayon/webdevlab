use redis::{Client, RedisResult};

pub fn init_client(redis_url: &str) -> RedisResult<Client> {
    let client = Client::open(redis_url)?;
    println!("✅ Connected to Redis");
    Ok(client)
}
