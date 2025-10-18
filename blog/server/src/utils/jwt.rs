use crate::config::AppConfig;
use chrono::{Duration, Utc};
use jsonwebtoken::{
    DecodingKey, EncodingKey, Header, TokenData, Validation, decode, encode, errors::Error,
};
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
pub struct TokenClaims {
    pub sub: i32,
    pub exp: i64,
    pub iat: i64,
}

pub struct JwtUtil;

impl JwtUtil {
    pub fn generate_access_token(
        user_id: i32,
        config: &AppConfig,
    ) -> Result<String, jsonwebtoken::errors::Error> {
        let now = Utc::now();
        let expires_in = now + Duration::seconds(config.jwt_expires_in);

        let claims = TokenClaims {
            sub: user_id,
            exp: expires_in.timestamp(),
            iat: now.timestamp(),
        };

        encode(
            &Header::default(),
            &claims,
            &EncodingKey::from_secret(config.jwt_secret.as_ref()),
        )
    }

    pub fn generate_refresh_token(
        user_id: i32,
        config: &AppConfig,
    ) -> Result<String, jsonwebtoken::errors::Error> {
        let now = Utc::now();
        let expires_in = now + Duration::seconds(config.refresh_token_expires_in);

        let claims = TokenClaims {
            sub: user_id,
            exp: expires_in.timestamp(),
            iat: now.timestamp(),
        };

        encode(
            &Header::default(),
            &claims,
            &EncodingKey::from_secret(config.jwt_secret.as_ref()),
        )
    }

    pub fn verify_token(
        token: &str,
        config: &AppConfig,
    ) -> Result<TokenClaims, jsonwebtoken::errors::Error> {
        let token_data = decode::<TokenClaims>(
            token,
            &DecodingKey::from_secret(config.jwt_secret.as_ref()),
            &Validation::default(),
        )?;

        Ok(token_data.claims)
    }

    // NEW: decode_access_token function
    pub fn decode_access_token(
        token: &str,
        config: &AppConfig,
    ) -> Result<TokenData<TokenClaims>, Error> {
        decode::<TokenClaims>(
            token,
            &DecodingKey::from_secret(config.jwt_secret.as_ref()),
            &Validation::default(),
        )
    }
}
