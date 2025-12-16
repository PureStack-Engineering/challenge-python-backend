# 🐍 PureStack Backend Engineering Challenge: The Microservice Protocol

**PureStack.es - Engineering Validation Protocol.**
> *"We are not interested in algorithmic puzzles. We audit Architecture, Concurrency, and Reliability."*

---

### 📋 Context & Mission
Welcome to the PureStack Technical Validation Protocol for Backend Engineering.
This assessment is designed to audit your ability to build **production-ready systems** using Python and FastAPI/Django.

**The Mission:** Develop a RESTful API for a **High-Frequency Transaction System**.
Imagine a service that receives financial transactions and needs to validate, store, and provide real-time statistics efficiently.

### 🚦 Certification Levels (Choose your Difficulty)
Your seniority is defined by your architectural choices, concurrency management, and code structure. State your target level in your Pull Request.

#### 🥉 Level 3: Essential / Mid-Level
* **Focus:** Functionality & Containerization.
* **Requirement:** A working API that passes the standard tests.
* **Tasks:**
    1.  **Endpoints:** Implement `POST /transactions` (Receive amount/timestamp) and `GET /stats` (Return sum/avg/max).
    2.  **Validation:** Use **Pydantic** models to strictly validate inputs (e.g., negative amounts not allowed).
    3.  **Persistence:** Store data in memory or SQLite.
    4.  **Docker:** Create a valid `Dockerfile` that starts the application successfully.
* **Deliverable:** A functional API where `pytest` returns GREEN.

#### 🥈 Level 2: Pro / Senior
* **Focus:** Clean Architecture, Async & Separation of Concerns.
* **Requirement:** Everything in Level 3 + **Service Layer & Dependency Injection**.
* **Extra Tasks:**
    1.  **Decoupling:** Do NOT put business logic inside the route handler (Controller). Implement a **Service Layer** and inject it using Dependency Injection (FastAPI `Depends`).
    2.  **Async Mastery:** Ensure all I/O operations (DB writes, etc.) use proper `async/await` syntax to not block the event loop.
    3.  **Error Handling:** Implement global exception handlers (Middleware) to return standard JSON errors instead of 500 crashes.
* **Deliverable:** A Clean Architecture codebase that is testable and readable.

#### 🥇 Level 1: Elite / Architect
* **Focus:** Algorithmic Efficiency (O(1)), Security & Integration Testing.
* **Requirement:** Everything above + **Constant Time Stats & JWT**.
* **Extra Tasks:**
    1.  **O(1) Complexity:** The `/stats` endpoint must return results in **Constant Time** (O(1)), regardless of whether there are 10 or 10 million transactions. *Hint: Update stats on write, don't iterate on read.*
    2.  **Security:** Implement a mechanism for **JWT Authentication** (Middleware). The `/transactions` endpoint should be protected.
    3.  **Integration Tests:** Add a separate test suite (`tests/integration`) that spins up a real database (or TestContainer) to verify the full flow.
* **Deliverable:** A high-performance system capable of handling high load with low latency.

---

### 🛠️ Tech Stack Requirements
* **Language:** Python 3.10+ (Strict Type Hinting is mandatory).
* **Framework:** FastAPI (Highly Recommended) or Django Ninja.
* **Containerization:** **Docker is mandatory.** A `Dockerfile` must be included.
* **Testing:** Pytest.

---

### 🚀 Execution Instructions

1.  **Fork** this repository.
2.  Install dependencies: `pip install -r requirements.txt`.
3.  Implement your solution inside the `src/` folder.
4.  Run local tests: `pytest`.
5.  **Dockerize** your solution and verify it runs.
6.  Submit via **Pull Request** stating your target Level.

### 🧪 Evaluation Criteria (PureStack Audit)

| Criteria | Weight | Audit Focus |
| :--- | :--- | :--- |
| **Architecture** | 30% | Separation of concerns (Routes vs Services). DI usage. |
| **Concurrency** | 25% | Proper `async` usage. Handling of race conditions (Level 1). |
| **Code Quality** | 25% | Type Hints (MyPy friendly), Pydantic usage, Clean Code. |
| **Containerization** | 20% | Does `docker build` work? Is the image optimized? |

---

### 🚨 Project Structure (Standard)
To ensure our **Automated Auditor** works, keep this structure:

```text
/
├── .github/
│   └── workflows/
│       └── audit.yml          # PureStack Audit System (CI Pipeline)
├── src/
│   ├── models/                # Data Transfer Objects (Place Pydantic Schemas here)
│   ├── services/              # Business Logic Layer (Place Core Logic here)
│   ├── __init__.py
│   └── main.py                # Application Entry Point (FastAPI App)
├── tests/
│   ├── __init__.py
│   └── test_api.py            # Validation Tests (Run 'pytest' to check your progress)
├── Dockerfile                 # Container Configuration (Required for Level 3)
├── requirements.txt           # Project Dependencies (FastAPI, Uvicorn, etc.)
└── README.md                  # Challenge Instructions
