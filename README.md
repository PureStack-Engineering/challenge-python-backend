# 🐍 PureStack Backend Engineering Challenge: The Microservice Protocol

### Context
Welcome to the PureStack Technical Validation Protocol.
This assessment is designed to audit your ability to build **production-ready backend systems**. We are not interested in algorithmic puzzles; we are interested in Architecture, Clean Code, and Reliability.

**⚠️ The Standard:** We expect code that could be deployed to production today. Meaning: Typed, Tested, and Dockerized.

---

### 🎯 The Objective
Develop a RESTful API (Microservice) that manages a **High-Load Transaction System**.
Imagine a system that receives financial transactions and needs to validate, store, and query them efficiently.

1.  **The API:** Create endpoints to:
    * `POST /transactions`: Receive a payload (amount, currency, timestamp, user_id).
    * `GET /stats`: Return real-time statistics (total amount, avg amount) for the last 60 seconds (or a configurable window).
    * `DELETE /transactions`: Clear data.
2.  **The Logic:** The system must handle concurrency safely.
3.  **The Persistence:** Use a database (PostgreSQL/SQLite) or an efficient in-memory structure if you can justify it.

### 🛠️ Tech Stack Requirements
* **Language:** Python 3.10+ (Strict Type Hinting required).
* **Framework:** FastAPI (Recommended) or Django Ninja.
* **Containerization:** **Docker is mandatory.** A `Dockerfile` (and `docker-compose.yml` if DB is used) must be included.
* **Testing:** `pytest` suite covering the core logic.

### 🧪 Evaluation Criteria (How we audit you)
We will clone your repo and run `docker compose up`. If it fails to start, the audit fails immediately. We look for:

1.  **Architecture:** Do you use Dependency Injection? Is the business logic decoupled from the API layer?
2.  **Asynchronous Concurrency:** Proper use of `async/await`.
3.  **Data Validation:** Usage of Pydantic models for robust input validation.
4.  **Testing Culture:** Are you testing edge cases (e.g., negative amounts, future dates)?

### 🚀 Getting Started

1.  **Fork** this repository.
2.  Design your architecture.
3.  Implement the solution in the `src/` folder.
4.  Write your tests.
5.  **Dockerize** the solution.
6.  Submit via Pull Request or Repo Link.

---

### 📂 Bonus Points (Elite Level)
* Implement **JWT Authentication** (even a mock one) for the endpoints.
* Use **Redis** for caching the `/stats` endpoint.


* Add a **GitHub Actions** workflow file that runs the tests automatically on push.

> **PureStack Engineering.** Validated by Code.
