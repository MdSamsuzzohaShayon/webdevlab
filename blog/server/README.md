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









Absolutely — your stack (**Actix Web + PostgreSQL + Redis + Nuxt.js**) is a very solid choice for a blog, especially if you want performance, scalability, and flexibility. Let's go step by step so you can build it professionally and future-proof it.

---

## ✅ 1. System Design (Architecture)

Think of your system as three layers:

### **1️⃣ Backend (Actix Web)**

* **Authentication & Authorization**

  * JWT-based authentication (access + refresh tokens).
  * Role-based permissions (`admin`, `author`, `reader`).

* **Blog API**

  * CRUD for posts, categories, tags.
  * Rich text or markdown storage.
  * Comment system (optional threaded comments).
  * Pagination + search + filtering.

* **Caching Layer** (via Redis)

  * Cache frequently accessed posts and home page.
  * Use Redis as a session store for logged-in users.
  * Implement cache invalidation on post update/delete.

---

### **2️⃣ Database (PostgreSQL)**

Use **normalized schema** + some denormalization for speed.
Here’s a simple schema to start with:

```sql
-- Users table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  role TEXT DEFAULT 'reader',
  created_at TIMESTAMP DEFAULT NOW()
);

-- Blog posts
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  author_id INT REFERENCES users(id),
  title TEXT NOT NULL,
  slug TEXT UNIQUE NOT NULL,
  content TEXT NOT NULL, -- store markdown or html
  status TEXT DEFAULT 'draft', -- draft/published
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Tags
CREATE TABLE tags (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL
);

-- Post <-> Tag many-to-many
CREATE TABLE post_tags (
  post_id INT REFERENCES posts(id),
  tag_id INT REFERENCES tags(id),
  PRIMARY KEY (post_id, tag_id)
);

-- Comments
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  post_id INT REFERENCES posts(id),
  user_id INT REFERENCES users(id),
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);
```

📌 **Performance tips:**

* Add **indexes** on `slug`, `author_id`, `created_at`.
* Consider **full-text search** using PostgreSQL `tsvector` for search functionality.

---

### **3️⃣ Frontend (Nuxt.js)**

* **SEO-first approach**: Nuxt is perfect because of SSR (Server-Side Rendering).
* **Dynamic Routes**:

  * `/blog/:slug` for individual posts.
  * `/tags/:tag` for tag filtering.
* **Markdown Rendering**:

  * Use `@nuxt/content` module or `remark/rehype` pipeline to render markdown.
  * Enable code syntax highlighting (`prismjs` or `shiki`).
* **Static Generation**:

  * Pre-generate posts that don’t change often to reduce backend load.

---

## ✅ 2. High-Performance Hosting Plans

### **Backend (Actix + Redis + Postgres)**

* **Budget / Fast Setup** → [Railway.app](https://railway.app) or [Render](https://render.com)

  * Deploy Actix as a Docker service.
  * Managed PostgreSQL + Redis.
* **Scalable / Production** → [Fly.io](https://fly.io) or \[Hetzner Cloud]

  * Deploy in multiple regions (low latency).
  * Self-host Redis + Postgres (or use managed services like Supabase for Postgres).
* **Enterprise / Extreme Scale** → AWS ECS + RDS + ElastiCache

### **Frontend (Nuxt.js)**

* Use **Vercel** or **Netlify** to deploy SSR/SSG Nuxt app with automatic CI/CD.
* Edge CDN built-in → very fast page loads.

---

## ✅ 3. Frontend Editor Handling (Coding Blog)

For a **developer blog** (with code blocks):

* Use a **Markdown-based editor** for content creation:

  * **TipTap** (best for WYSIWYG + markdown hybrid)
  * **Editor.js** (modular block editor)
  * Or even a simple textarea + markdown preview.
* Enable:

  * Code highlighting (`Prism.js`, `Highlight.js`, or `Shiki`)
  * Image uploads (store on S3 / Cloudflare R2)
  * Math (if needed) → KaTeX or MathJax

---

## ✅ 4. Redis Usage (Best Practices)

* **Session Store**

  * Store JWT refresh tokens or session IDs.
* **Cache Layer**

  * Cache popular blog posts:

    ```rust
    // pseudo
    let key = format!("post:{}", slug);
    if let Some(cached) = redis.get(key) {
        return cached;
    }
    let post = db.query(...);
    redis.set_ex(key, post, 3600); // expire in 1 hour
    ```
* **Rate Limiting**

  * Use Redis counters for API rate limiting (prevent abuse).

---

## ✅ 5. Other Recommendations

* **Logging & Monitoring**

  * Use `tracing` crate in Actix for structured logging.
  * Add error tracking (Sentry, Logtail).

* **Testing**

  * Write integration tests for API endpoints using `actix_web::test`.

* **Security**

  * Use HTTPS everywhere (Cloudflare free plan is great).
  * Sanitize user input to prevent XSS (especially for comments).

* **Scalability**

  * Run Actix with multiple workers (`workers = num_cpus::get()`).
  * Horizontal scaling: containerize app with Docker.

---

postgres=# CREATE DATABASE webdevlab_blog;
CREATE DATABASE
postgres=# GRANT ALL PRIVILEGES ON DATABASE webdevlab_blog TO shayon;
GRANT
postgres=# \c webdevlab_blog;
You are now connected to database "webdevlab_blog" as user "postgres".
shayon@shayonhost:~$ sudo -u postgres psql



 1009  cargo install sqlx-cli --no-default-features --features postgres,rustls
 1010  ~/.cargo/bin
 1011  sqlx --version
 1012  sqlx migrate add 20250911_create_users_posts_tags_comments
 1013  # 1️⃣ Users table
 1014  sqlx migrate add 20250911_create_users
 1015  # 2️⃣ Posts table
 1016  sqlx migrate add 20250911_create_posts
 1017  # 3️⃣ Tags + post_tags table
 1018  sqlx migrate add 20250911_create_tags_and_post_tags
 1019  # 4️⃣ Comments table
 1020  sqlx migrate add 20250911_create_comments


  1021  sqlx migrate add create_posts
 1022  sqlx migrate add create_tags
 1023  sqlx migrate add create_post_tags
 1024  sqlx migrate add create_comments
 1025  sqlx migrate add create_categories
 1026  sqlx migrate add add_category_to_posts




  1001  sudo -u postgres psql
 1002  cd Documents/web/webdevlab/blog
 1003  sudo -u postgres psql
 1004  cd server/
 1005  rm -rf migrations/
 1006  mkdir migrations
 1007  sqlx migrate add create_users
 1008  export DATABASE_URL=postgres://shayon:Test1234@localhost:5432/webdevlab_blog
 1009  sqlx migrate run
 1010  sqlx migrate info




