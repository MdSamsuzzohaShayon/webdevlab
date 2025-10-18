use crate::{
    errors::AppError,
    models::category::{CategoryResponse, CreateCategory, UpdateCategory},
    services::category_service::CategoryService,
};
use actix_web::{HttpResponse, delete, get, post, put, web};
use utoipa::IntoParams;
use validator::Validate;

#[utoipa::path(
    post,
    path = "/api/categories",
    request_body = CreateCategory,
    responses(
        (status = 201, description = "Category created successfully"),
        (status = 400, description = "Validation error"),
        (status = 401, description = "Unauthorized")
    )
)]
#[post("")]
pub async fn create_category(
    category_service: web::Data<CategoryService>,
    category_data: web::Json<CreateCategory>,
) -> Result<HttpResponse, AppError> {
    category_data
        .validate()
        .map_err(|e| AppError::ValidationError(e.to_string()))?;

    let category = category_service
        .create_category(category_data.into_inner())
        .await?;

    Ok(HttpResponse::Created().json(category))
}

#[utoipa::path(
    get,
    path = "/api/categories",
    responses(
        (status = 200, description = "List of categories", body = [CategoryResponse])
    )
)]
#[get("")]
pub async fn get_all_categories(
    category_service: web::Data<CategoryService>,
) -> Result<HttpResponse, AppError> {
    let categories = category_service.get_all_categories().await?;

    Ok(HttpResponse::Ok().json(categories))
}

#[utoipa::path(
    get,
    path = "/api/categories/{id}",
    params(
        ("id" = i32, Path, description = "Category ID")
    ),
    responses(
        (status = 200, description = "Category details", body = CategoryResponse),
        (status = 404, description = "Category not found")
    )
)]
#[get("/{id}")]
pub async fn get_category(
    category_service: web::Data<CategoryService>,
    path: web::Path<i32>,
) -> Result<HttpResponse, AppError> {
    let category_id = path.into_inner();
    let category = category_service.get_category(category_id).await?;

    Ok(HttpResponse::Ok().json(category))
}

#[utoipa::path(
    get,
    path = "/api/categories/slug/{slug}",
    params(
        ("slug" = String, Path, description = "Category slug")
    ),
    responses(
        (status = 200, description = "Category details", body = CategoryResponse),
        (status = 404, description = "Category not found")
    )
)]
#[get("/slug/{slug}")]
pub async fn get_category_by_slug(
    category_service: web::Data<CategoryService>,
    path: web::Path<String>,
) -> Result<HttpResponse, AppError> {
    let slug = path.into_inner();
    let category = category_service.get_category_by_slug(slug).await?;

    Ok(HttpResponse::Ok().json(category))
}

#[utoipa::path(
    put,
    path = "/api/categories/{id}",
    params(
        ("id" = i32, Path, description = "Category ID")
    ),
    request_body = UpdateCategory,
    responses(
        (status = 200, description = "Category updated successfully"),
        (status = 400, description = "Validation error"),
        (status = 401, description = "Unauthorized"),
        (status = 404, description = "Category not found")
    )
)]
#[put("/{id}")]
pub async fn update_category(
    category_service: web::Data<CategoryService>,
    path: web::Path<i32>,
    update_data: web::Json<UpdateCategory>,
) -> Result<HttpResponse, AppError> {
    if let Err(e) = update_data.validate() {
        return Err(AppError::ValidationError(e.to_string()));
    }

    let category_id = path.into_inner();
    let category = category_service
        .update_category(category_id, update_data.into_inner())
        .await?;

    Ok(HttpResponse::Ok().json(category))
}

#[utoipa::path(
    delete,
    path = "/api/categories/{id}",
    params(
        ("id" = i32, Path, description = "Category ID")
    ),
    responses(
        (status = 200, description = "Category deleted successfully"),
        (status = 401, description = "Unauthorized"),
        (status = 404, description = "Category not found")
    )
)]
#[delete("/{id}")]
pub async fn delete_category(
    category_service: web::Data<CategoryService>,
    path: web::Path<i32>,
) -> Result<HttpResponse, AppError> {
    let category_id = path.into_inner();
    category_service.delete_category(category_id).await?;

    Ok(HttpResponse::Ok().json(serde_json::json!({
        "message": "Category deleted successfully"
    })))
}

pub fn init_routes(cfg: &mut web::ServiceConfig) {
    cfg.service(create_category)
        .service(get_all_categories)
        .service(get_category)
        .service(get_category_by_slug)
        .service(update_category)
        .service(delete_category);
}
