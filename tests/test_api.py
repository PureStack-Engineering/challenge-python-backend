from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    """Sanity check to ensure app can start"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_order_success():
    """
    Test valid order creation.
    Expected: 200 OK and correct total calculation.
    """
    payload = {
        "item_name": "Laptop",
        "quantity": 2,
        "price": 1000.50
    }
    response = client.post("/orders", json=payload)
    
    # ❌ This will fail initially (404 Not Found)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    
    assert "order_id" in data
    assert data["total_price"] == 2001.0  # 2 * 1000.50

def test_create_order_invalid_data():
    """
    Test validation logic (Level 3).
    Expected: 422 Unprocessable Entity for negative quantity.
    """
    payload = {
        "item_name": "Bad Item",
        "quantity": -5, 
        "price": 100
    }
    response = client.post("/orders", json=payload)
    
    # Pydantic should catch this automatically
    assert response.status_code == 422
