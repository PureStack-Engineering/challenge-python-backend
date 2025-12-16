from fastapi import FastAPI

# Initialize the App
app = FastAPI(title="PureStack Microservice")

@app.get("/health")
def health_check():
    """
    Level 1: Basic Health Check.
    Expected: 200 OK, {"status": "ok"}
    """
    return {"status": "ok"}

# TODO: Implement POST /orders endpoint here
# Requirements:
# 1. Receive JSON payload (use Pydantic model)
# 2. Validate data
# 3. Process logic in services/
# 4. Return 200 OK with order_id
