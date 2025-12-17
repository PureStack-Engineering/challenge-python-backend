from fastapi import FastAPI
import logging

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="PureStack Order Service")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# TODO: Implement POST /orders here
# Remember: Move logic to src/services/ for Level 2
