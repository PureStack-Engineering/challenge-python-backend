from fastapi import FastAPI

app = FastAPI(title="PureStack Microservice")

@app.get("/health")
def health_check():
    """Level 1: Basic Health Check."""
    return {"status": "ok"}

# TODO: Implement POST /orders logic here for Level 2
# Use src/models for Pydantic schemas
# Use src/services for business logic
