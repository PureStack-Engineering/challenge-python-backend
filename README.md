# 🐍 PureStack Backend Engineering Challenge: The Microservice Protocol

**PureStack.es - Engineering Validation Protocol.**
> *"We don't audit algorithms. We audit Architecture, Clean Code, and Containerization."*

---

### 📋 Context & Mission
Welcome to the PureStack Technical Validation Protocol for Backend Engineering.
This assessment audits your ability to build **production-ready systems** using Python and FastAPI.

**The Mission:** You are building the core **Order Processing Microservice**.
The system must receive incoming orders, validate the data structure, calculate totals based on business rules, and return a confirmed response.

### 🚦 Certification Levels (Choose your Difficulty)
Your seniority is defined by your architectural choices and how you structure your code. State your target level in your Pull Request.

#### 🥉 Level 3: Essential / Mid-Level
* **Focus:** Functionality & Validation.
* **Requirement:** A working API that passes the `pytest` checks.
* **Tasks:**
    1.  **Endpoint:** Implement `POST /orders`.
    2.  **Logic:** The endpoint must accept a JSON payload (Item, Quantity, Price) and return an Order ID + Total Price (`Quantity * Price`).
    3.  **Validation:** Use **Pydantic** to reject invalid data (e.g., negative quantity or price).
    4.  **Structure:** The API must run successfully via `uvicorn`.
* **Deliverable:** A functional API where `pytest` returns GREEN.

#### 🥈 Level 2: Pro / Senior
* **Focus:** Clean Architecture & Separation of Concerns.
* **Requirement:** Everything in Level 3 + **Service Layer Pattern**.
* **Extra Tasks:**
    1.  **Decoupling:** Do NOT put business logic inside the route handler (`main.py`). Move the logic to `src/services/`.
    2.  **DTOs:** Define strict Pydantic models in `src/models/` for both Request and Response.
    3.  **Dependency Injection:** Inject the service into the controller using FastAPI's `Depends`.
* **Deliverable:** A codebase where the "Controller" only handles HTTP, and the "Service" handles Logic.

#### 🥇 Level 1: Elite / Architect
* **Focus:** Containerization & Production Standards.
* **Requirement:** Everything above + **Optimized Docker**.
* **Extra Tasks:**
    1.  **Dockerization:** Complete the `Dockerfile`. The image must build successfully and start the app.
    2.  **Optimization:** Ensure the Docker image is lightweight (use `slim` or `alpine` variants) and does not run as root user if possible.
    3.  **Logging:** Implement structured logging (JSON format) instead of simple `print()` statements for better observability in containers.
* **Deliverable:** A container-ready microservice suitable for Kubernetes deployment.

---

### 🛠️ Tech Stack Requirements
* **Language:** Python 3.10+.
* **Framework:** FastAPI.
* **Validation:** Pydantic V2.
* **Testing:** Pytest / TestClient.
* **Container:** Docker.

---

### 🚀 Execution Instructions

1.  **Fork** this repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Architect your solution:**
    * `src/models/`: Place your Pydantic schemas here.
    * `src/services/`: Place your calculation logic here.
    * `src/main.py`: Wire everything together.
4.  Run validation tests:
    ```bash
    pytest tests/
    ```
5.  **Level 1 Only:** Build and run via Docker:
    ```bash
    docker build -t purestack-backend .
    docker run -p 8000:8000 purestack-backend
    ```
6.  Submit via **Pull Request**.

> **Note:** You will see a ❌ (**Red Cross**) initially because the `/orders` endpoint returns 404. Your goal is to write the code that turns it ✅ (**Green**).

---

### 📝 Audit & Validation Rules (Strict)

> **⚠️ The "Async-First" Policy**
>
> Our automated auditor (`audit.yml`) enforces strict quality rules. Your PR will be automatically rejected if:
>
> 1.  **Blocking Code:** Usage of `time.sleep()` is strictly forbidden in our Async FastAPI environment. You must use `await asyncio.sleep()`.
> 2.  **Dirty Logging:** `print()` statements are forbidden in production code. Use the standard `logging` module or `structlog`.
> 3.  **Docker Failure:** Your `Dockerfile` must build without errors (Level 1 requirement).
> 4.  **Structure Integrity:** Do not delete `src/services` or `src/models`. The auditor expects a Clean Architecture layout.

---

### 🧪 Evaluation Criteria (PureStack Audit)

| Criteria | Weight | Audit Focus |
| :--- | :--- | :--- |
| **Correctness** | 30% | Does `POST /orders` calculate the total correctly? (5 * 20.5 = 102.5) |
| **Architecture** | 30% | Did you separate Models, Services, and Controllers? (Level 2) |
| **Code Quality** | 20% | Type Hints usage, Async best practices, and Pydantic validation. |
| **DevOps** | 20% | Is the Dockerfile correct and efficient? (Level 1) |

---

### 🚨 Project Structure (Strict)
To ensure our **Automated Auditor** works, keep this structure:

```text
/
├── .github/workflows/   # PureStack Audit System
├── src/
│   ├── models/          # <--- Pydantic Schemas (Required)
│   ├── services/        # <--- Business Logic (Required)
│   ├── __init__.py
│   └── main.py          # <--- Entry Point
├── tests/
│   ├── __init__.py
│   └── test_api.py      # Validation Logic
├── Dockerfile           # <--- Complete this for Level 1
├── requirements.txt     # Dependencies
└── README.md
