from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check_exists():
    """
    Sanity Check: Ensures the app can start and respond.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_order_logic():
    """
    The Challenge: This test will FAIL until the candidate implements the logic.
    """
    payload = {
        "item_id": "ITM-9988",
        "quantity": 5,
        "price": 20.5
    }
    
    # This expects a POST /orders endpoint
    response = client.post("/orders", json=payload)
    
    # 🚨 This assertion will fail with 404 until implemented
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}. Did you create the endpoint?"
    
    data = response.json()
    assert "order_id" in data
    assert data["total_price"] == 102.5  # 5 * 20.5
