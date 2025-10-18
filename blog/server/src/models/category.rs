use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use sqlx::FromRow;
use utoipa::ToSchema;
use validator::Validate;

#[derive(Debug, Serialize, Deserialize, FromRow)]
pub struct Category {
    pub id: i32,
    pub name: String,
    pub slug: String,
    pub description: Option<String>,
    pub created_at: DateTime<Utc>,
    pub updated_at: DateTime<Utc>,
}

#[derive(Debug, Serialize, Deserialize, Validate, ToSchema)]
pub struct CreateCategory {
    #[validate(length(min = 1, max = 100))]
    pub name: String,

    #[validate(length(min = 1, max = 120))]
    pub slug: String,

    pub description: Option<String>,
}

#[derive(Debug, Serialize, Deserialize, Validate, ToSchema)]
pub struct UpdateCategory {
    #[validate(length(min = 1, max = 100))]
    pub name: Option<String>,

    #[validate(length(min = 1, max = 120))]
    pub slug: Option<String>,

    pub description: Option<String>,
}

#[derive(Debug, Serialize, Deserialize, ToSchema)]
pub struct CategoryResponse {
    pub id: i32,
    pub name: String,
    pub slug: String,
    pub description: Option<String>,
    #[schema(value_type = String, format = "date-time")]
    pub created_at: String,
    #[schema(value_type = String, format = "date-time")]
    pub updated_at: String,
}

impl From<Category> for CategoryResponse {
    fn from(category: Category) -> Self {
        CategoryResponse {
            id: category.id,
            name: category.name,
            slug: category.slug,
            description: category.description,
            created_at: category.created_at.to_rfc3339(),
            updated_at: category.updated_at.to_rfc3339(),
        }
    }
}
