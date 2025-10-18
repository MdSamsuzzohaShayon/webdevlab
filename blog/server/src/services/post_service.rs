use crate::{
    errors::AppError,
    models::post::{CreatePost, Post, PostResponse, PostWithDetails, UpdatePost},
};
use sqlx::PgPool;

#[derive(Clone)]
pub struct PostService {
    pool: PgPool,
}

impl PostService {
    pub fn new(pool: PgPool) -> Self {
        Self { pool }
    }

    pub async fn create_post(
        &self,
        post_data: CreatePost,
        author_id: i32,
    ) -> Result<PostResponse, AppError> {
        let post = sqlx::query_as::<_, Post>(
            "INSERT INTO posts (title, content, author_id, category_id, published) 
             VALUES ($1, $2, $3, $4, $5) 
             RETURNING *",
        )
        .bind(&post_data.title)
        .bind(&post_data.content)
        .bind(author_id)
        .bind(post_data.category_id)
        .bind(post_data.published.unwrap_or(false))
        .fetch_one(&self.pool)
        .await?;

        self.get_post_with_details(post.id).await
    }

    pub async fn get_post(&self, post_id: i32) -> Result<PostResponse, AppError> {
        self.get_post_with_details(post_id).await
    }

    pub async fn get_all_posts(&self, published_only: bool) -> Result<Vec<PostResponse>, AppError> {
        let query = if published_only {
            "SELECT p.*, u.first_name as author_first_name, u.last_name as author_last_name, 
                    u.email as author_email, c.name as category_name
             FROM posts p
             LEFT JOIN users u ON p.author_id = u.id
             LEFT JOIN categories c ON p.category_id = c.id
             WHERE p.published = true
             ORDER BY p.created_at DESC"
        } else {
            "SELECT p.*, u.first_name as author_first_name, u.last_name as author_last_name, 
                    u.email as author_email, c.name as category_name
             FROM posts p
             LEFT JOIN users u ON p.author_id = u.id
             LEFT JOIN categories c ON p.category_id = c.id
             ORDER BY p.created_at DESC"
        };

        let posts = sqlx::query_as::<_, PostWithDetails>(query)
            .fetch_all(&self.pool)
            .await?;

        Ok(posts.into_iter().map(PostResponse::from).collect())
    }

    pub async fn get_posts_by_author(&self, author_id: i32) -> Result<Vec<PostResponse>, AppError> {
        let posts = sqlx::query_as::<_, PostWithDetails>(
            "SELECT p.*, u.first_name as author_first_name, u.last_name as author_last_name, 
                    u.email as author_email, c.name as category_name
             FROM posts p
             LEFT JOIN users u ON p.author_id = u.id
             LEFT JOIN categories c ON p.category_id = c.id
             WHERE p.author_id = $1
             ORDER BY p.created_at DESC",
        )
        .bind(author_id)
        .fetch_all(&self.pool)
        .await?;

        Ok(posts.into_iter().map(PostResponse::from).collect())
    }

    pub async fn get_posts_by_category(
        &self,
        category_id: i32,
        published_only: bool,
    ) -> Result<Vec<PostResponse>, AppError> {
        let query = if published_only {
            "SELECT p.*, u.first_name as author_first_name, u.last_name as author_last_name, 
                    u.email as author_email, c.name as category_name
             FROM posts p
             LEFT JOIN users u ON p.author_id = u.id
             LEFT JOIN categories c ON p.category_id = c.id
             WHERE p.category_id = $1 AND p.published = true
             ORDER BY p.created_at DESC"
        } else {
            "SELECT p.*, u.first_name as author_first_name, u.last_name as author_last_name, 
                    u.email as author_email, c.name as category_name
             FROM posts p
             LEFT JOIN users u ON p.author_id = u.id
             LEFT JOIN categories c ON p.category_id = c.id
             WHERE p.category_id = $1
             ORDER BY p.created_at DESC"
        };

        let posts = sqlx::query_as::<_, PostWithDetails>(query)
            .bind(category_id)
            .fetch_all(&self.pool)
            .await?;

        Ok(posts.into_iter().map(PostResponse::from).collect())
    }

    pub async fn update_post(
        &self,
        post_id: i32,
        update_data: UpdatePost,
        author_id: i32,
    ) -> Result<PostResponse, AppError> {
        // Verify post exists and belongs to author
        let existing_post =
            sqlx::query_as::<_, Post>("SELECT * FROM posts WHERE id = $1 AND author_id = $2")
                .bind(post_id)
                .bind(author_id)
                .fetch_optional(&self.pool)
                .await?;

        if existing_post.is_none() {
            return Err(AppError::NotFound(
                "Post not found or unauthorized".to_string(),
            ));
        }

        // Build dynamic update query
        let mut query = "UPDATE posts SET ".to_string();
        let mut params: Vec<String> = Vec::new();
        let mut counter = 1;

        if let Some(title) = &update_data.title {
            params.push(format!("title = ${}", counter));
            counter += 1;
        }
        if let Some(content) = &update_data.content {
            params.push(format!("content = ${}", counter));
            counter += 1;
        }
        if update_data.category_id.is_some() {
            params.push(format!("category_id = ${}", counter));
            counter += 1;
        }
        if update_data.published.is_some() {
            params.push(format!("published = ${}", counter));
            counter += 1;
        }

        if params.is_empty() {
            return self.get_post_with_details(post_id).await;
        }

        params.push("updated_at = CURRENT_TIMESTAMP".to_string());
        query.push_str(&params.join(", "));
        query.push_str(" WHERE id = $");
        query.push_str(&counter.to_string());
        query.push_str(" RETURNING *");

        // Build query parameters
        let mut query_builder = sqlx::query(&query);

        if let Some(title) = &update_data.title {
            query_builder = query_builder.bind(title);
        }
        if let Some(content) = &update_data.content {
            query_builder = query_builder.bind(content);
        }
        if let Some(category_id) = update_data.category_id {
            query_builder = query_builder.bind(category_id);
        }
        if let Some(published) = update_data.published {
            query_builder = query_builder.bind(published);
        }
        query_builder = query_builder.bind(post_id);

        let _post = query_builder.execute(&self.pool).await?;

        self.get_post_with_details(post_id).await
    }

    pub async fn delete_post(&self, post_id: i32, author_id: i32) -> Result<(), AppError> {
        let result = sqlx::query("DELETE FROM posts WHERE id = $1 AND author_id = $2")
            .bind(post_id)
            .bind(author_id)
            .execute(&self.pool)
            .await?;

        if result.rows_affected() == 0 {
            return Err(AppError::NotFound(
                "Post not found or unauthorized".to_string(),
            ));
        }

        Ok(())
    }

    async fn get_post_with_details(&self, post_id: i32) -> Result<PostResponse, AppError> {
        let post = sqlx::query_as::<_, PostWithDetails>(
            "SELECT p.*, u.first_name as author_first_name, u.last_name as author_last_name, 
                    u.email as author_email, c.name as category_name
             FROM posts p
             LEFT JOIN users u ON p.author_id = u.id
             LEFT JOIN categories c ON p.category_id = c.id
             WHERE p.id = $1",
        )
        .bind(post_id)
        .fetch_one(&self.pool)
        .await?;

        Ok(PostResponse::from(post))
    }
}
