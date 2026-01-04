# 🐳 Docker: El Contenedor de Envíos

![Difficulty](https://img.shields.io/badge/Dificultad-Importante-blue)
![Reading Time](https://img.shields.io/badge/Lectura-12_min-blue)

## 👶 1. Explicación para Niños (ELI5)

Antes, para mover una casa (tu App), tenías que desmontarla ladrillo a ladrillo y rezar para reconstruirla igual en otro lugar. 🏚️
Con **Docker**, metes la casa entera con muebles y aire acondicionado dentro de un **Contenedor Mágico**. 📦
El contenedor se abre igual en tu laptop, en un servidor en China o en la Luna. **"Funciona en mi máquina" = "Funciona en todas partes".**

---

## 🔬 2. Deep Dive: Layered File System (UnionFS)

Una imagen de Docker no es un bloque sólido. Son capas (Layers) como una cebolla. 🧅
1.  **Base Layer**: Ubuntu/Alpine (El SO mínimo).
2.  **Deps Layer**: Python instalado.
3.  **App Layer**: Tu código copiado.

**Docker Cache**: Si cambias tu código (Capa 3), Docker **NO** reconstruye las Capas 1 y 2. Las reutiliza. ¡Por eso es tan rápido!

---

## 📊 3. Visualización: Las Capas de la Cebolla

```mermaid
graph BT
    L1["Kernel del Host (Linux)"]
    L2["Base Image: Python 3.10 Slim"]
    L3["Dependencies: pip install -r requirements.txt"]
    L4["Source Code: COPY . /app"]
    L5["Container: Writable Layer"]
    
    L1 --> L2
    L2 --> L3
    L3 --> L4
    L4 --> L5
    
    style L5 fill:#ccffcc,stroke:#00aa00
    note right of L2: Read Only 🔒
    note right of L3: Read Only 🔒
    note right of L5: Read Write ✏️
```

---

## 👩‍💻 4. Tutorial Interactivo: Dockerizando la Pizzeria

Vamos a crear el archivo `Dockerfile` perfecto para nuestra API de pizzas.

```dockerfile
# 1. IMAGEN BASE (El cimiento)
# Usamos 'slim' porque es ligera (aprox 100MB) vs la full (900MB)
FROM python:3.10-slim

# 2. DIRECTORIO DE TRABAJO (La cocina)
WORKDIR /app

# 3. INSTALAR DEPENDENCIAS (Primero esto para aprovechar caché)
# Si copias todo el código primero, cualquier cambio romperá el caché de dependencias.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. COPIAR CÓDIGO (Los ingredientes)
COPY . .

# 5. COMANDO DE ARRANQUE (Abrir restaurante)
# Usamos 'uvicorn' para producción
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

### Comandos Esenciales

```bash
# PASO A: Construir el contenedor (Cocinar)
# -t pone nombre (tag)
# . dice "busca el Dockerfile aquí"
docker build -t mi-pizzeria:v1 .

# PASO B: Correr el contenedor (Servir)
# -p 8000:80 -> Conecta el puerto 8000 de MI laptop al 80 del contenedor
docker run -p 8000:80 mi-pizzeria:v1
```

### 🧠 ¿Qué aprendimos?
1.  **Orden importa**: Copiar `requirements.txt` *antes* del código fuente acelera los builds futuros dramáticamente.
2.  **Aislamiento**: Dentro del contenedor, la app cree que es dueña única del servidor (Puerto 80). Desde fuera, nosotros decidimos dónde mapearla (Puerto 8000).

---
[⬅️ Anterior: Clean Code](../03_Clean_Code/03_guia_solid.md) | [Siguiente: Web API 🌍](../04_Especializacion/01_Web/01_guia_web.md)
