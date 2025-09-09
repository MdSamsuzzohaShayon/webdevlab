# 🚀 Actix Web Backend – Auth & Blog API

A scalable **Rust backend** built with [Actix Web](https://actix.rs/) featuring:

- 🔐 **Auth API** → Signup, Login, JWT sessions (stored in Redis)
- 📝 **Blog API** → Full CRUD for posts (PostgreSQL via `sqlx` or `sea-orm`)
- 🗄 **PostgreSQL** → Persistent storage for blog content and users
- ⚡ **Redis** → Caching + session management for fast authentication

---

## 📂 Project Structure

```

src/
├── api/           # Route handlers (auth, blog)
├── models/        # Database models
├── services/      # Business logic (auth, blog, cache)
├── db/            # Database/Redis connection pools
├── utils/         # Helpers (JWT, password hashing)
├── config.rs      # App configuration (env, DB URLs)
├── errors.rs      # Error handling
└── main.rs        # Entry point

````

---

## ⚙️ Setup

### 1. Install Rust
Ensure you have the latest stable Rust:
```bash
rustup update
````

### 2. Clone Repository

```bash
git clone https://github.com/your-username/actix-backend.git
cd actix-backend
```

### 3. Setup Environment

Create a `.env` file in the project root:

```env
DATABASE_URL=postgres://user:password@localhost:5432/blogdb
REDIS_URL=redis://127.0.0.1:6379
PORT=8080
JWT_SECRET=super_secret_key
```

### 4. Run PostgreSQL & Redis

Using Docker:

```bash
docker run --name blog-postgres -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=blogdb -p 5432:5432 -d postgres
docker run --name blog-redis -p 6379:6379 -d redis
```

### 5. Run Backend

```bash
cargo run
```

Server will start on:

```
http://localhost:8080
```

---

## 🛠 API Endpoints

### Auth API

* `POST /api/auth/signup` → Create new user
* `POST /api/auth/login` → Authenticate & get JWT
* `POST /api/auth/logout` → Invalidate session

### Blog API

* `GET /api/posts` → Get all posts
* `GET /api/posts/{id}` → Get post by ID
* `POST /api/posts` → Create new post
* `PUT /api/posts/{id}` → Update a post
* `DELETE /api/posts/{id}` → Delete a post

---

## ✅ Quick Test

After running the server:

```bash
curl http://localhost:8080/hey
```

Expected:

```
Hello, Actix Web!
```

---

## 📦 Tech Stack

* [Rust](https://www.rust-lang.org/)
* [Actix Web](https://actix.rs/)
* [SQLx](https://github.com/launchbadge/sqlx) or [SeaORM](https://www.sea-ql.org/SeaORM/)
* [Redis](https://redis.io/)
* [dotenvy](https://crates.io/crates/dotenvy)

---

## 🔮 Future Improvements

* Add user roles & permissions
* Rate limiting with Redis
* Blog categories & comments
* OpenAPI/Swagger documentation

---

## 📝 License

MIT License © 2025 **Md Samsuzzoha Shayon**

