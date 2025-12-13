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

### 🚨 CRITICAL: Project Structure
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
