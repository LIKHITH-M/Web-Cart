# 🛒 Spring Boot Web Cart — Full-Stack E-Commerce Application

## Overview
This is a full-stack E-Commerce Application built using a **Java Spring Boot** backend and a **React (Vite)** frontend. The application allows users to securely register, log in, browse products, search by keyword, view product images, and manage a shopping cart. It demonstrates a secure, stateless monolithic architecture using **Spring Security with JWT (JSON Web Tokens)** for authentication and a **PostgreSQL** database for persistent storage.

---

## 🏗️ Architecture & Request Flow
The system uses a unified client-server architecture where the frontend directly interacts with the backend REST API:

1. **Client (React App)** sends a request to the Spring Boot REST API.
2. **Security**: If it is a protected route, the request passes through the `JwtFilter` to validate the `Authorization: Bearer <token>`.
3. **Controller**: Spring Boot Controllers (`ProductController`, `AuthController`) route the request to the appropriate Service layers.
4. **Data Access**: Services interact with the PostgreSQL database via Spring Data JPA repositories.
5. **Response**: JSON responses or Blob image data are returned to the React frontend to be rendered dynamically.

---

## 📦 System Breakdown

### 🌐 Frontend Client (Vite + React)
* **Routing**: Uses `react-router-dom` to navigate between Home, Cart, Add Product, and Login screens.
* **Auth State**: Uses Axios interceptors to automatically attach the JWT token (stored in `localStorage`) to every outgoing API request.
* **UX**: Automatically redirects unauthorized users back to the login page.

### 🛡️ Authentication & Security Profile
* **Statelessness**: Disables CSRF and sessions to remain stateless.
* **JWT Logic**: Automatically generates a dynamic 256-bit **HS256** secret key on server startup for signing tokens.
* **User Details**: Implements `MyUserDetailsService` to manage security, passwords, and user sessions.

### 🛒 Core Backend API (Spring Boot)
* **Database**: `likhith` (PostgreSQL).
* **Key Endpoints**:
    * `POST /api/auth/register` & `/api/auth/login` — Account management and JWT generation.
    * `GET /api/products` — Fetch all products.
    * `GET /api/product/{id}/image` — Stream product image database blobs directly to the browser.
    * `POST /api/product` — Create and update products using `multipart/form-data` for image uploads.

---

## 🛠️ Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **Java 17+** | Backend programming language |
| **Spring Boot** | Backend application framework |
| **Spring Security** | Authentication and authorization |
| **JJWT** | JSON Web Token generation and validation |
| **PostgreSQL** | Relational database storage |
| **React (Vite ⚡)** | Frontend UI framework |
| **Axios** | Handling HTTP requests and global interceptors |
| **Lombok** | Boilerplate code reduction (`@Data`) |

---
