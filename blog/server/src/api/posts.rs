use crate::{
    errors::AppError,
    models::post::{CreatePost, PostResponse, UpdatePost},
    services::post_service::PostService,
};
use actix_web::{HttpResponse, delete, get, post, put, web};
use utoipa::IntoParams;
use validator::Validate;

#[utoipa::path(
    post,
    path = "/api/posts",
    request_body = CreatePost,
    responses(
        (status = 201, description = "Post created successfully"),
        (status = 400, description = "Validation error"),
        (status = 401, description = "Unauthorized")
    )
)]
#[post("")]
pub async fn create_post(
    post_service: web::Data<PostService>,
    user_id: web::ReqData<i32>,
    post_data: web::Json<CreatePost>,
) -> Result<HttpResponse, AppError> {
    post_data
        .validate()
        .map_err(|e| AppError::ValidationError(e.to_string()))?;

    let post = post_service
        .create_post(post_data.into_inner(), *user_id)
        .await?;

    Ok(HttpResponse::Created().json(post))
}

#[utoipa::path(
    get,
    path = "/api/posts",
    params(
        ("published_only" = Option<bool>, Query, description = "Filter only published posts")
    ),
    responses(
        (status = 200, description = "List of posts", body = [PostResponse])
    )
)]
#[get("")]
pub async fn get_all_posts(
    post_service: web::Data<PostService>,
    query: web::Query<std::collections::HashMap<String, String>>,
) -> Result<HttpResponse, AppError> {
    let published_only = query
        .get("published_only")
        .and_then(|v| v.parse::<bool>().ok())
        .unwrap_or(true);

    let posts = post_service.get_all_posts(published_only).await?;

    Ok(HttpResponse::Ok().json(posts))
}

#[utoipa::path(
    get,
    path = "/api/posts/{id}",
    params(
        ("id" = i32, Path, description = "Post ID")
    ),
    responses(
        (status = 200, description = "Post details", body = PostResponse),
        (status = 404, description = "Post not found")
    )
)]
#[get("/{id}")]
pub async fn get_post(
    post_service: web::Data<PostService>,
    path: web::Path<i32>,
) -> Result<HttpResponse, AppError> {
    let post_id = path.into_inner();
    let post = post_service.get_post(post_id).await?;

    Ok(HttpResponse::Ok().json(post))
}

#[utoipa::path(
    get,
    path = "/api/posts/author/{author_id}",
    params(
        ("author_id" = i32, Path, description = "Author ID")
    ),
    responses(
        (status = 200, description = "List of posts by author", body = [PostResponse])
    )
)]
#[get("/author/{author_id}")]
pub async fn get_posts_by_author(
    post_service: web::Data<PostService>,
    path: web::Path<i32>,
) -> Result<HttpResponse, AppError> {
    let author_id = path.into_inner();
    let posts = post_service.get_posts_by_author(author_id).await?;

    Ok(HttpResponse::Ok().json(posts))
}

#[utoipa::path(
    get,
    path = "/api/posts/category/{category_id}",
    params(
        ("category_id" = i32, Path, description = "Category ID"),
        ("published_only" = Option<bool>, Query, description = "Filter only published posts")
    ),
    responses(
        (status = 200, description = "List of posts by category", body = [PostResponse])
    )
)]
#[get("/category/{category_id}")]
pub async fn get_posts_by_category(
    post_service: web::Data<PostService>,
    path: web::Path<i32>,
    query: web::Query<std::collections::HashMap<String, String>>,
) -> Result<HttpResponse, AppError> {
    let category_id = path.into_inner();
    let published_only = query
        .get("published_only")
        .and_then(|v| v.parse::<bool>().ok())
        .unwrap_or(true);

    let posts = post_service
        .get_posts_by_category(category_id, published_only)
        .await?;

    Ok(HttpResponse::Ok().json(posts))
}

#[utoipa::path(
    put,
    path = "/api/posts/{id}",
    params(
        ("id" = i32, Path, description = "Post ID")
    ),
    request_body = UpdatePost,
    responses(
        (status = 200, description = "Post updated successfully"),
        (status = 400, description = "Validation error"),
        (status = 401, description = "Unauthorized"),
        (status = 404, description = "Post not found")
    )
)]
#[put("/{id}")]
pub async fn update_post(
    post_service: web::Data<PostService>,
    user_id: web::ReqData<i32>,
    path: web::Path<i32>,
    update_data: web::Json<UpdatePost>,
) -> Result<HttpResponse, AppError> {
    if let Err(e) = update_data.validate() {
        return Err(AppError::ValidationError(e.to_string()));
    }

    let post_id = path.into_inner();
    let post = post_service
        .update_post(post_id, update_data.into_inner(), *user_id)
        .await?;

    Ok(HttpResponse::Ok().json(post))
}

#[utoipa::path(
    delete,
    path = "/api/posts/{id}",
    params(
        ("id" = i32, Path, description = "Post ID")
    ),
    responses(
        (status = 200, description = "Post deleted successfully"),
        (status = 401, description = "Unauthorized"),
        (status = 404, description = "Post not found")
    )
)]
#[delete("/{id}")]
pub async fn delete_post(
    post_service: web::Data<PostService>,
    user_id: web::ReqData<i32>,
    path: web::Path<i32>,
) -> Result<HttpResponse, AppError> {
    let post_id = path.into_inner();
    post_service.delete_post(post_id, *user_id).await?;

    Ok(HttpResponse::Ok().json(serde_json::json!({
        "message": "Post deleted successfully"
    })))
}

pub fn init_routes(cfg: &mut web::ServiceConfig) {
    cfg.service(create_post)
        .service(get_all_posts)
        .service(get_post)
        .service(get_posts_by_author)
        .service(get_posts_by_category)
        .service(update_post)
        .service(delete_post);
}
