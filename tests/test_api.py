import pytest
import sys
import os
from fastapi.testclient import TestClient

# --- CONFIGURACIÓN DEL ENTORNO ---
# Añadimos la raíz al path para encontrar el código del candidato
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# --- IMPORTACIÓN ROBUSTA DE LA APP ---
# Buscamos 'app' dentro de 'main.py' o 'src/main.py'
try:
    from main import app
except ImportError:
    try:
        from src.main import app
    except ImportError:
        pytest.fail("❌ No se encontró el archivo 'main.py' con la instancia 'app = FastAPI()'.")

client = TestClient(app)

def test_architecture_exists():
    """Valida que la app de FastAPI se ha instanciado correctamente."""
    assert app is not None

def test_health_check():
    """
    PRUEBA 1: HEALTH CHECK
    Todo microservicio debe tener un endpoint raíz o /health que devuelva 200.
    """
    response = client.get("/")
    # Si el candidato usó /health en vez de /, probamos ese también
    if response.status_code == 404:
        response = client.get("/health")
    
    assert response.status_code == 200, f"❌ La API no responde 200 OK en / ni en /health. Código recibido: {response.status_code}"
    # Verificamos que devuelva un JSON válido
    assert response.headers["content-type"] == "application/json"

def test_endpoint_structure():
    """
    PRUEBA 2: DOCUMENTACIÓN AUTOMÁTICA
    FastAPI genera /docs automáticamente. Si esto falla, no es FastAPI o está mal configurado.
    """
    response = client.get("/docs")
    assert response.status_code == 200, "❌ No se encuentra la documentación Swagger en /docs."

# --- PRUEBA DE LÓGICA (PERSONALIZABLE) ---
# Si tu challenge pide un endpoint específico (ej: POST /candidates), descomenta esto:
"""
def test_create_candidate_flow():
    payload = {"name": "Test User", "skills": ["Python", "FastAPI"]}
    response = client.post("/candidates", json=payload)
    assert response.status_code in [200, 201], "❌ Falló la creación de candidato."
    data = response.json()
    assert data["name"] == "Test User"
"""
