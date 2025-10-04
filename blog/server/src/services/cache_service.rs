use redis::{Client, Commands};
use crate::errors::AppError;

#[derive(Clone)]
pub struct CacheService {
    client: Client,
}

impl CacheService {
    pub fn new(client: Client) -> Self {
        Self { client }
    }

    pub fn store_refresh_token(&self, user_id: i32, token: &str, expires_in: u64) -> Result<(), AppError> {
        let key = format!("refresh_token:{}", user_id);
        let mut con = self.client.get_connection()?;
        // Explicitly use RedisResult
        let _: () = redis::cmd("SETEX")
        .arg(&key)
        .arg(expires_in)
        .arg(token)
        .query(&mut con)?;
            Ok(())
    }

    pub fn get_refresh_token(&self, user_id: i32) -> Result<String, AppError> {
        let key = format!("refresh_token:{}", user_id);
        let mut con = self.client.get_connection()?;
        let token: String = con.get(&key)?;
        Ok(token)
    }

    pub fn delete_refresh_token(&self, user_id: i32) -> Result<(), AppError> {
        let key = format!("refresh_token:{}", user_id);
        let mut con = self.client.get_connection()?;
        let _: () = redis::cmd("DEL").arg(&key).query(&mut con)?;
        Ok(())
    }

    pub fn store_verification_token(&self, email: &str, token: &str, expires_in: u64) -> Result<(), AppError> {
        let key = format!("verify_email:{}", email);
        let mut con = self.client.get_connection()?;
        // Explicitly use RedisResult
        let _: () = redis::cmd("SETEX")
        .arg(&key)
        .arg(expires_in)
        .arg(token)
        .query(&mut con)?;
        Ok(())
    }

    pub fn get_verification_token(&self, email: &str) -> Result<String, AppError> {
        let key = format!("verify_email:{}", email);
        let mut con = self.client.get_connection()?;
        let token: String = con.get(&key)?;
        Ok(token)
    }

    pub fn store_reset_token(&self, email: &str, token: &str, expires_in: u64) -> Result<(), AppError> {
        let key = format!("reset_token:{}", email);
        let mut con = self.client.get_connection()?;
        // Explicitly use RedisResult
        let _: () = redis::cmd("SETEX")
        .arg(&key)
        .arg(expires_in)
        .arg(token)
        .query(&mut con)?;
        Ok(())
    }

    pub fn get_reset_token(&self, email: &str) -> Result<String, AppError> {
        let key = format!("reset_token:{}", email);
        let mut con = self.client.get_connection()?;
        let token: String = con.get(&key)?;
        Ok(token)
    }

    pub fn delete_reset_token(&self, email: &str) -> Result<(), AppError> {
        let key = format!("reset_token:{}", email);
        let mut con = self.client.get_connection()?;
        let _: () = redis::cmd("DEL").arg(&key).query(&mut con)?;
        Ok(())
    }
}