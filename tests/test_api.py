from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    """Level 1: Validate environment is running."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_order_flow():
    """Level 2: Validate business logic."""
    payload = {"item_id": "PS-101", "quantity": 2, "price": 50.0}
    
    # 🚨 ESTO FALLARÁ (404) hasta que el candidato lo programe
    response = client.post("/orders", json=payload)
    
    assert response.status_code == 200, "❌ El endpoint POST /orders no existe aún."
    data = response.json()
    assert "order_id" in data
    assert data["total_price"] == 100.0
