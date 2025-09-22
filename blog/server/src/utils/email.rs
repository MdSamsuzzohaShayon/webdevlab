use lettre::{Message, SmtpTransport, Transport};
use lettre::transport::smtp::authentication::Credentials;
use crate::config::AppConfig;

pub struct EmailUtil;

impl EmailUtil {
    pub async fn send_verification_email(
        config: &AppConfig,
        email: &str,
        token: &str,
    ) -> Result<(), String> {
        let verification_url = format!("{}/verify-email?token={}", config.frontend_url, token);
        
        let email_body = format!(
            "Please click the link to verify your email: {}",
            verification_url
        );

        Self::send_email(config, email, "Verify Your Email", &email_body).await
    }

    pub async fn send_password_reset_email(
        config: &AppConfig,
        email: &str,
        token: &str,
    ) -> Result<(), String> {
        let reset_url = format!("{}/reset-password?token={}", config.frontend_url, token);
        
        let email_body = format!(
            "Please click the link to reset your password: {}",
            reset_url
        );

        Self::send_email(config, email, "Reset Your Password", &email_body).await
    }

    async fn send_email(
        config: &AppConfig,
        to: &str,
        subject: &str,
        body: &str,
    ) -> Result<(), String> {
        let email = Message::builder()
            .from(config.from_email.parse().map_err(|e| format!("Invalid from email: {}", e))?)
            .to(to.parse().map_err(|e| format!("Invalid to email: {}", e))?)
            .subject(subject)
            .body(body.to_string())
            .map_err(|e| format!("Email build error: {}", e))?;

        let creds = Credentials::new(
            config.smtp_username.clone(),
            config.smtp_password.clone(),
        );

        let mailer = SmtpTransport::relay(&config.smtp_host)
            .map_err(|e| format!("SMTP relay error: {}", e))?
            .port(config.smtp_port)
            .credentials(creds)
            .build();

        mailer.send(&email)
            .map_err(|e| format!("Email send error: {}", e))?;

        Ok(())
    }
}