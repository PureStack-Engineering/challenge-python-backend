# 🐍 PureStack Backend Engineering Challenge: The Microservice Protocol

### Context
Welcome to the **PureStack Technical Validation Protocol**.
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

---

**Requirement:** Your FastAPI instance in `src/main.py` must be named `app`.

### 🛠️ Tech Stack Requirements
* **Language:** Python 3.10+ (Strict Type Hinting required).
* **Framework:** FastAPI (Recommended) or Django Ninja.
* **Containerization:** **Docker is mandatory.** A `Dockerfile` (and `docker-compose.yml` if DB is used) must be included.
* **Testing:** The repo comes with a basic `pytest` suite. You must pass it **AND** extend it.

### 🧪 Evaluation Criteria (How we audit you)
We will clone your repo and run the automated audit. We look for:

* **Green Lights:** Your code must pass the provided GitHub Actions workflow (`audit.yml`).
* **Architecture:** Do you use Dependency Injection? Is the business logic decoupled from the API layer?
* **Asynchronous Concurrency:** Proper use of `async/await`.
* **Data Validation:** Usage of Pydantic models for robust input validation.

### 🚀 Getting Started
1. **Fork** this repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the health check locally: `pytest`.
4. Implement your solution inside the `src/` folder.
5. **Dockerize** the solution.
6. Submit via Pull Request.

### 📂 Bonus Points (Elite Level)
* Implement **JWT Authentication** (even a mock one) for the endpoints.
* Use **Redis** for caching the `/stats` endpoint.
* Add **Integration Tests** in a separate folder.

### 🚨 CRITICAL: Project Structurerggrg
To ensure our **Automated Auditor** works correctly, you **MUST** follow this structure.
We have provided a skeleton in `src/main.py`.

```text
/
├── .github/workflows/   # PureStack Audit System (DO NOT TOUCH)
├── src/
│   ├── __init__.py
│   └── main.py          # <--- YOUR ENTRY POINT (app = FastAPI())
├── tests/               # Validation Tests (You can add more, but don't break existing ones)
├── Dockerfile           # <--- REQUIRED
├── requirements.txt
└── README.md

