use crate::{
    errors::AppError,
    models::category::{Category, CategoryResponse, CreateCategory, UpdateCategory},
};
use sqlx::{PgPool, Row};

#[derive(Clone)]
pub struct CategoryService {
    pool: PgPool,
}

impl CategoryService {
    pub fn new(pool: PgPool) -> Self {
        Self { pool }
    }

    pub async fn create_category(
        &self,
        category_data: CreateCategory,
    ) -> Result<CategoryResponse, AppError> {
        // Check if category with same name or slug already exists
        let existing_category =
            sqlx::query_as::<_, Category>("SELECT * FROM categories WHERE name = $1 OR slug = $2")
                .bind(&category_data.name)
                .bind(&category_data.slug)
                .fetch_optional(&self.pool)
                .await?;

        if existing_category.is_some() {
            return Err(AppError::ValidationError(
                "Category with this name or slug already exists".to_string(),
            ));
        }

        let category = sqlx::query_as::<_, Category>(
            "INSERT INTO categories (name, slug, description) 
             VALUES ($1, $2, $3) 
             RETURNING *",
        )
        .bind(&category_data.name)
        .bind(&category_data.slug)
        .bind(&category_data.description)
        .fetch_one(&self.pool)
        .await?;

        Ok(CategoryResponse::from(category))
    }

    pub async fn get_category(&self, category_id: i32) -> Result<CategoryResponse, AppError> {
        let category = sqlx::query_as::<_, Category>("SELECT * FROM categories WHERE id = $1")
            .bind(category_id)
            .fetch_one(&self.pool)
            .await?;

        Ok(CategoryResponse::from(category))
    }

    pub async fn get_category_by_slug(&self, slug: String) -> Result<CategoryResponse, AppError> {
        let category = sqlx::query_as::<_, Category>("SELECT * FROM categories WHERE slug = $1")
            .bind(slug)
            .fetch_one(&self.pool)
            .await?;

        Ok(CategoryResponse::from(category))
    }

    pub async fn get_all_categories(&self) -> Result<Vec<CategoryResponse>, AppError> {
        let categories = sqlx::query_as::<_, Category>("SELECT * FROM categories ORDER BY name")
            .fetch_all(&self.pool)
            .await?;

        Ok(categories.into_iter().map(CategoryResponse::from).collect())
    }

    pub async fn update_category(
        &self,
        category_id: i32,
        update_data: UpdateCategory,
    ) -> Result<CategoryResponse, AppError> {
        // Check if category exists
        let existing_category =
            sqlx::query_as::<_, Category>("SELECT * FROM categories WHERE id = $1")
                .bind(category_id)
                .fetch_optional(&self.pool)
                .await?;

        if existing_category.is_none() {
            return Err(AppError::NotFound("Category not found".to_string()));
        }

        // Check for duplicate name/slug if updating
        if let Some(name) = &update_data.name {
            let duplicate = sqlx::query_as::<_, Category>(
                "SELECT * FROM categories WHERE (name = $1 OR slug = $2) AND id != $3",
            )
            .bind(name)
            .bind(update_data.slug.as_ref().unwrap_or(name)) // Use slug if provided, else name
            .bind(category_id)
            .fetch_optional(&self.pool)
            .await?;

            if duplicate.is_some() {
                return Err(AppError::ValidationError(
                    "Category with this name or slug already exists".to_string(),
                ));
            }
        }

        // Build dynamic update query
        let mut query = "UPDATE categories SET ".to_string();
        let mut params: Vec<String> = Vec::new();
        let mut counter = 1;

        if let Some(name) = &update_data.name {
            params.push(format!("name = ${}", counter));
            counter += 1;
        }
        if let Some(slug) = &update_data.slug {
            params.push(format!("slug = ${}", counter));
            counter += 1;
        }
        if update_data.description.is_some() {
            params.push(format!("description = ${}", counter));
            counter += 1;
        }

        if params.is_empty() {
            return self.get_category(category_id).await;
        }

        params.push("updated_at = CURRENT_TIMESTAMP".to_string());
        query.push_str(&params.join(", "));
        query.push_str(" WHERE id = $");
        query.push_str(&counter.to_string());
        query.push_str(" RETURNING *");

        // Build query parameters
        let mut query_builder = sqlx::query(&query);

        if let Some(name) = &update_data.name {
            query_builder = query_builder.bind(name);
        }
        if let Some(slug) = &update_data.slug {
            query_builder = query_builder.bind(slug);
        }
        if let Some(description) = &update_data.description {
            query_builder = query_builder.bind(description);
        }
        query_builder = query_builder.bind(category_id);

        let category = query_builder
            .map(|row: sqlx::postgres::PgRow| Category {
                id: row.get("id"),
                name: row.get("name"),
                slug: row.get("slug"),
                description: row.get("description"),
                created_at: row.get("created_at"),
                updated_at: row.get("updated_at"),
            })
            .fetch_one(&self.pool)
            .await?;

        Ok(CategoryResponse::from(category))
    }

    pub async fn delete_category(&self, category_id: i32) -> Result<(), AppError> {
        let result = sqlx::query("DELETE FROM categories WHERE id = $1")
            .bind(category_id)
            .execute(&self.pool)
            .await?;

        if result.rows_affected() == 0 {
            return Err(AppError::NotFound("Category not found".to_string()));
        }

        Ok(())
    }
}
