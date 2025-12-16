# Usamos una imagen ligera de Python
FROM python:3.10-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalamos dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código fuente
COPY src/ ./src/

# Comando para arrancar la app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
