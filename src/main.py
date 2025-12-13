from fastapi import FastAPI

# Metadatos profesionales
app = FastAPI(
    title="PureStack Backend Challenge",
    version="1.0.0"
)

# Endpoint Raíz (Este pasará el test de Health Check)
@app.get("/")
def health_check():
    return {"status": "operational", "service": "purestack-backend"}

# NOTA PARA EL CANDIDATO:
# Aquí debajo debes implementar tus endpoints.
# - POST /transactions
# - GET /stats
# - DELETE /transactions
