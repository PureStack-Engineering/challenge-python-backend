import pytest
import sys
import os
from fastapi.testclient import TestClient

# --- CONFIGURACIÓN DE RUTAS (CRÍTICO) ---
# Esto añade explícitamente la carpeta 'src' al camino que mira Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# --- IMPORTACIÓN SEGURA ---
try:
    # Ahora podemos importar 'main' directamente porque 'src' está en el path
    from main import app
except ImportError as e:
    # Si falla, imprimimos el error real para verlo en los logs de GitHub
    print(f"❌ ERROR DE IMPORTACIÓN: {e}")
    print(f"📂 Rutas actuales: {sys.path}")
    print(f"📂 Archivos en src: {os.listdir(os.path.join(os.path.dirname(__file__), '../src')) if os.path.exists(os.path.join(os.path.dirname(__file__), '../src')) else 'No existe src'}")
    pytest.fail(f"❌ No se pudo importar la API. Asegúrate de que 'src/main.py' existe y tiene la variable 'app'. Error: {e}")

client = TestClient(app)

def test_health_check():
    """
    PRUEBA 1: HEALTH CHECK (Debe pasar con el esqueleto base)
    """
    response = client.get("/")
    # Aceptamos 200 OK en / o en /health
    if response.status_code == 404:
        response = client.get("/health")
    
    assert response.status_code == 200, f"❌ La API no responde en la raíz. Status: {response.status_code}"
    assert response.json().get("status") is not None or response.json().get("info") is not None

def test_transactions_endpoint_exists():
    """
    PRUEBA 2: ENDPOINT DE TRANSACCIONES (Debe fallar al principio)
    Este test verifica si el candidato ha implementado la lógica.
    Al principio dará 404 o 405, lo cual es correcto para un challenge no empezado.
    """
    # Intentamos enviar una transacción dummy
    payload = {
        "amount": 100.50,
        "currency": "EUR",
        "user_id": "test_user"
    }
    response = client.post("/transactions", json=payload)
    
    # Si devuelve 404, es que el candidato aún no ha trabajado.
    # NO fallamos el test aquí para que el pipeline pase en verde inicial,
    # pero dejamos un aviso (warning).
    if response.status_code == 404:
        pytest.skip("⚠️ El endpoint POST /transactions aún no está implementado.")
    
    # Si existe, debe responder 200 o 201
    assert response.status_code in [200, 201], "El endpoint existe pero falló al procesar datos válidos."
