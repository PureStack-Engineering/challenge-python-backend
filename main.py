from fastapi import FastAPI

# Inicializamos la app para que el servidor de pruebas pueda arrancarla
app = FastAPI(
    title="PureStack Backend Challenge",
    description="API para validación técnica de candidatos.",
    version="1.0.0"
)

# TODO: Implementar los endpoints requeridos en el README.
# Pista: El auditor buscará un Health Check en "/" o "/health".

@app.get("/")
def root():
    return {"info": "PureStack API Challenge. Implement logic here."}
