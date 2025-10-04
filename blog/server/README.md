# 🚀 Actix Web Backend – Authentication & Blog API

A high-performance, production-ready Rust backend built with [Actix Web](https://actix.rs/) featuring robust authentication and full blog management capabilities.

## ✨ Features

- 🔐 **JWT Authentication** - Secure signup/login with Redis session storage
- 📝 **Blog Management** - Complete CRUD operations for posts with categories and tags
- 🗄 **PostgreSQL Integration** - Persistent data storage with SQLx
- ⚡ **Redis Caching** - High-performance session management and caching
- 🛡 **Security First** - Password hashing, input validation, and CORS protection
- 📊 **Structured Logging** - Comprehensive logging with tracing
- 🧪 **Testing Ready** - Integration tests and health checks
- 🐳 **Docker Ready** - Containerized deployment

## 🏗 System Architecture

```
Client (Nuxt.js) → Actix Web API → Redis (Cache/Sessions) → PostgreSQL (Data)
```

## 📁 Project Structure

```bash
src/
├── api/
│   ├── auth.rs          # Authentication routes
│   ├── blog.rs          # Blog post routes
│   └── mod.rs
├── models/
│   ├── user.rs          # User data models
│   ├── post.rs          # Post data models
│   └── mod.rs
├── services/
│   ├── auth.rs          # Authentication logic
│   ├── blog.rs          # Blog business logic
│   ├── cache.rs         # Redis operations
│   └── mod.rs
├── db/
│   ├── postgres.rs      # Database connection pool
│   ├── redis.rs         # Redis connection
│   └── mod.rs
├── utils/
│   ├── jwt.rs           # JWT token handling
│   ├── password.rs      # Password hashing
│   └── mod.rs
├── config.rs            # Application configuration
├── errors.rs            # Custom error handling
├── middleware.rs        # Custom middleware (auth, logging)
└── main.rs              # Application entry point
```

## 🚀 Quick Start

### Prerequisites

- Rust 1.70+ ([install](https://rustup.rs/))
- PostgreSQL 14+
- Redis 7+

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mdsamsuzzohashayon/webdevlab.git
   cd webdevlab/blog/server
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your configuration:
   ```env
   # Server
   PORT=8080
   HOST=0.0.0.0
   RUST_LOG=debug

   # Database
   DATABASE_URL=postgres://user:password@localhost:5432/webdevlab_blog
   REDIS_URL=redis://127.0.0.1:6379

   # Security
   JWT_SECRET=your-super-secret-key-change-in-production
   JWT_EXPIRES_IN=3600
   BCRYPT_COST=12
   ```

3. **Set up databases with Docker**
   ```bash
   # PostgreSQL
   docker run --name blog-postgres \
     -e POSTGRES_USER=user \
     -e POSTGRES_PASSWORD=password \
     -e POSTGRES_DB=webdevlab_blog \
     -p 5432:5432 -d postgres:15-alpine

   # Redis
   docker run --name blog-redis \
     -p 6379:6379 -d redis:7-alpine
   ```

4. **Run database migrations**
   ```bash
   # Install SQLx CLI if not already installed
   cargo install sqlx-cli --no-default-features --features postgres,rustls

   # Run migrations
   sqlx migrate run
   ```

5. **Start the application**
   ```bash
   # Development
   cargo run

   # Production build
   cargo build --release
   ./target/release/actix-backend
   ```

The server will start at `http://localhost:8080`

## 🗄 Database Schema

### Core Tables
- **users** - User accounts and authentication
- **posts** - Blog posts with content and metadata
- **categories** - Post categorization
- **tags** & **post_tags** - Tagging system for posts
- **comments** - Post comments with threading support

## 📚 API Documentation

### Authentication Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `POST` | `/api/auth/signup` | Register new user | ❌ |
| `POST` | `/api/auth/login` | User login | ❌ |
| `POST` | `/api/auth/logout` | User logout | ✅ |
| `POST` | `/api/auth/refresh` | Refresh JWT token | ✅ |
| `GET` | `/api/auth/me` | Get current user | ✅ |

### Blog Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/posts` | List posts (with pagination) | ❌ |
| `GET` | `/api/posts/{id}` | Get post by ID | ❌ |
| `GET` | `/api/posts/slug/{slug}` | Get post by slug | ❌ |
| `POST` | `/api/posts` | Create new post | ✅ |
| `PUT` | `/api/posts/{id}` | Update post | ✅ |
| `DELETE` | `/api/posts/{id}` | Delete post | ✅ |

### Management Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Health check |
| `GET` | `/metrics` | Application metrics |

## 🧪 Testing

```bash
# Run unit tests
cargo test

# Run integration tests
cargo test -- --test-threads=1

# Test with coverage
cargo tarpaulin --ignore-tests
```

## 🐳 Docker Deployment

```dockerfile
FROM rust:1.70-alpine as builder
WORKDIR /app
COPY . .
RUN cargo build --release

FROM alpine:latest
RUN addgroup -S app && adduser -S app -G app
USER app
COPY --from=builder /app/target/release/actix-backend /usr/local/bin/
EXPOSE 8080
CMD ["actix-backend"]
```

Build and run:
```bash
docker build -t actix-backend .
docker run -p 8080:8080 --env-file .env actix-backend
```

## 🔧 Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DATABASE_URL` | - | PostgreSQL connection string |
| `REDIS_URL` | `redis://127.0.0.1:6379` | Redis connection URL |
| `PORT` | `8080` | Server port |
| `HOST` | `0.0.0.0` | Server host |
| `JWT_SECRET` | - | Secret for JWT signing |
| `JWT_EXPIRES_IN` | `3600` | JWT expiration in seconds |
| `RUST_LOG` | `info` | Logging level |

## 🛠 Development

### Code Quality
```bash
# Format code
cargo fmt

# Lint code
cargo clippy

# Check dependencies
cargo audit
```

### Database Operations
```bash
# Create new migration
sqlx migrate add migration_name

# Run migrations
sqlx migrate run

# Revert migration
sqlx migrate revert
```

## 📊 Performance

- **Actix Web**: Asynchronous, actor-based web framework
- **Connection Pooling**: Database and Redis connection reuse
- **Caching Strategy**: Multi-layer caching with Redis
- **Compression**: Gzip compression for HTTP responses

## 🔮 Roadmap

- [ ] OpenAPI/Swagger documentation
- [ ] Rate limiting with Redis
- [ ] Email verification
- [ ] Password reset functionality
- [ ] Advanced search with PostgreSQL full-text
- [ ] File upload service
- [ ] Admin dashboard API
- [ ] Social authentication (Google, GitHub)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- 📧 Email: [your-email@domain.com]
- 🐛 Issues: [GitHub Issues](https://github.com/your-username/actix-backend/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/your-username/actix-backend/discussions)

---

**Built with ❤️ using Rust and Actix Web**

<div align="center">

*⭐ Star this repo if you find it helpful!*

</div>