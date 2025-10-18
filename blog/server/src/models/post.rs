use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use sqlx::FromRow;
use utoipa::ToSchema;
use validator::Validate;

#[derive(Debug, Serialize, Deserialize, FromRow)]
pub struct Post {
    pub id: i32,
    pub title: String,
    pub content: String,
    pub author_id: i32,
    pub category_id: Option<i32>,
    pub published: bool,
    pub created_at: DateTime<Utc>,
    pub updated_at: DateTime<Utc>,
}

#[derive(Debug, Serialize, Deserialize, Validate, ToSchema)]
pub struct CreatePost {
    #[validate(length(min = 1, max = 255))]
    pub title: String,

    #[validate(length(min = 1))]
    pub content: String,

    pub category_id: Option<i32>,
    pub published: Option<bool>,
}

#[derive(Debug, Serialize, Deserialize, Validate, ToSchema)]
pub struct UpdatePost {
    #[validate(length(min = 1, max = 255))]
    pub title: Option<String>,

    #[validate(length(min = 1))]
    pub content: Option<String>,

    pub category_id: Option<i32>,
    pub published: Option<bool>,
}

#[derive(Debug, Serialize, Deserialize, FromRow)]
pub struct PostWithDetails {
    pub id: i32,
    pub title: String,
    pub content: String,
    pub author_id: i32,
    pub author_first_name: String,
    pub author_last_name: String,
    pub author_email: String,
    pub category_id: Option<i32>,
    pub category_name: Option<String>,
    pub published: bool,
    pub created_at: DateTime<Utc>,
    pub updated_at: DateTime<Utc>,
}

#[derive(Debug, Serialize, Deserialize, ToSchema)]
pub struct PostResponse {
    pub id: i32,
    pub title: String,
    pub content: String,
    pub author_id: i32,
    pub author_name: String,
    pub author_email: String,
    pub category_id: Option<i32>,
    pub category_name: Option<String>,
    pub published: bool,
    #[schema(value_type = String, format = "date-time")]
    pub created_at: String,
    #[schema(value_type = String, format = "date-time")]
    pub updated_at: String,
}

impl From<PostWithDetails> for PostResponse {
    fn from(post: PostWithDetails) -> Self {
        PostResponse {
            id: post.id,
            title: post.title,
            content: post.content,
            author_id: post.author_id,
            author_name: format!("{} {}", post.author_first_name, post.author_last_name),
            author_email: post.author_email,
            category_id: post.category_id,
            category_name: post.category_name,
            published: post.published,
            created_at: post.created_at.to_rfc3339(),
            updated_at: post.updated_at.to_rfc3339(),
        }
    }
}

// Also implement From<Post> for PostResponse for cases where we have a Post without details
impl From<Post> for PostResponse {
    fn from(post: Post) -> Self {
        PostResponse {
            id: post.id,
            title: post.title,
            content: post.content,
            author_id: post.author_id,
            author_name: "".to_string(), // Will be filled by service layer
            author_email: "".to_string(), // Will be filled by service layer
            category_id: post.category_id,
            category_name: None,
            published: post.published,
            created_at: post.created_at.to_rfc3339(),
            updated_at: post.updated_at.to_rfc3339(),
        }
    }
}
