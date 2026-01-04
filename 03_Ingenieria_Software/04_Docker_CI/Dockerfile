# Este es un ejemplo real de un Dockerfile para una app de Python

# 1. Imagen Base (El sistema operativo mínimo con Python ya instalado)
FROM python:3.10-slim

# 2. Directorio de Trabajo (Creamos una carpeta dentro del contenedor)
WORKDIR /app

# 3. Copiamos los requisitos primero (Para aprovechar la caché de Docker)
# Truco experto: Si no cambias requirements.txt, Docker no repite este paso lento.
COPY requirements.txt .

# 4. Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos el resto del código
COPY . .

# 6. Comando por defecto al iniciar el contenedor
CMD ["python", "main.py"]
