# Web Dev Lab

A full-stack platform with three interconnected parts:

1. **Main Website:** [webdevlab.org](https://webdevlab.org)  
2. **Blog:** [blog.webdevlab.org](https://blog.webdevlab.org)  
3. **Forum:** [forum.webdevlab.org](https://forum.webdevlab.org)  

This project aims to provide a modern developer-focused platform featuring a blog, forum, course-selling system, and an advanced authentication mechanism.

---

## 📌 Main Website (webdevlab.org)

### ✅ Features
- Course selling platform
- Blog integration ([blog.webdevlab.org](https://blog.webdevlab.org))
- Short tutorials & guides
- Developer team / career opportunity portal
- Advanced cookie-based authentication with refresh token support
- Forum integration ([forum.webdevlab.org](https://forum.webdevlab.org))
- User roles: **Admin**, **Student**, **Viewer**
- Full SEO optimization for Nuxt.js pages

### 🛠 Tech Stack
- **Frontend:** Nuxt.js (with Bootstrap for UI)
- **Backend:** Django
- **Database:** PostgreSQL
- **Auth:** Cookie + Refresh Token flow
- **Editor:** Quill text editor
- **Internationalization:** [Intl](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)

### 📝 Todo
- [ ] Add unit & integration tests (Django + Nuxt.js)
- [ ] Fix linting issues (Django + Nuxt.js)
- [ ] Seed data into the database
- [ ] Complete frontend design with Bootstrap
- [ ] Implement mail service for **contact@webdevlab.com**

---

## 🚀 Running the Main Website

### Frontend Setup
```sh
cd client
npm install
npm run dev
````

Frontend will be available at **[http://localhost:3000](http://localhost:3000)**

---

## 📰 Blog (blog.webdevlab.org)

### 🛠 Tech Stack

* **Backend:** Rust (Actix Web)
* **Frontend:** Nuxt.js
* **Database:** PostgreSQL
* **Cache:** Redis

### ▶️ Running Without Docker

```sh
# Backend
cd blog/server
cargo run

# Frontend
cd blog/client
npm install
npm run dev
```

* Backend runs at: **[http://localhost:8000/hey](http://localhost:8000/hey)**
* Frontend runs at: **[http://localhost:3001](http://localhost:3001)**

### 🐳 Running With Docker

*Coming soon — will include Docker setup instructions for full-stack development.*

---

## 🧑‍💻 Contribution

Contributions are welcome!
Please open an issue or submit a pull request with clear descriptions of your changes.

---

## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](./LICENSE) file for details.

```
