# 🧪 Entornos: El Laboratorio Aislado

![Difficulty](https://img.shields.io/badge/Dificultad-Importante-blue)
![Reading Time](https://img.shields.io/badge/Lectura-10_min-blue)

## 👶 1. Explicación para Niños (ELI5)

Imagina que tienes dos experimentos: 
1.  Un volcán de bicarbonato. 🌋
2.  Una planta delicada. 🌿

Si mezclas los ingredientes de los dos en la misma mesa (Tu Sistema Global), el vinagre del volcán matará a la planta.
**Solución**: Usa mesas separadas (**Entornos Virtuales**).

---

## 🔬 2. Deep Dive: Site-Packages

Cuando haces `import numpy`, Python busca en una carpeta especial llamada `site-packages`.
- **Global**: `/usr/lib/python3.10/site-packages` (Compartido por todo el sistema).
- **Virtual**: `.venv/lib/python3.10/site-packages` (Privado).

Al activar un entorno, simplemente cambias la variable `PATH` y `PYTHONPATH` para que Python mire primero en la carpeta privada.

---

## 📊 3. Visualización: Dependency Hell

```mermaid
graph TD
    System[Python Global] --> LibA_V1[Librería A (v1.0)]
    
    Project1[Proyecto Antiguo] --> LibA_V1
    
    Project2[Proyecto Nuevo] -- Requiere v2.0 --> LibA_V2[Librería A (v2.0)]
    
    style LibA_V1 fill:#ffcccc
    style LibA_V2 fill:#ccffcc
    
    Note[🚨 CONFLICTO! No pueden coexistir en Global]
```

---

## 👩‍💻 4. Tutorial Interactivo: Poetry

Poetry es herramientas de gestión moderna. Vamos a simular su uso.

```toml
# ARCHIVO: pyproject.toml (La Receta)

[tool.poetry]
name = "mi-super-app"
version = "0.1.0"
description = "Una app que hace café"

[tool.poetry.dependencies]
python = "^3.10"
requests = "^2.28"  # Quiero la versión 2.28 o superior, pero menor a 3.0
flask = "*"         # Dame la última versión que exista

[tool.poetry.dev-dependencies]
pytest = "^7.0"     # Solo para mí (desarrollador), no para el usuario final.
```

### Comandos Esenciales (Cheat Sheet)

1.  `poetry init`: Crea el archivo de receta.
2.  `poetry add pandas`: Descarga pandas, lo mete en la carpeta aislada, y lo anota en la receta.
3.  `poetry shell`: "Entra" a la mesa de trabajo aislada (Activa el entorno).
4.  `poetry lock`: Congela las versiones exactas (crea `poetry.lock`) para que tu compañero instale BIT-A-BIT lo mismo que tú.

### 🧠 ¿Por qué poetry.lock?
Si yo digo "instala requests 2.28", puede que hoy sea la 2.28.1 y mañana la 2.28.2.
El **Lockfile** guarda: "Instalé requests 2.28.1 con el hash SHA256 8a7b3...".
Garantiza **Reproducibilidad Total**.

---
[⬅️ Anterior: Inspector](../01_Testing/01_guia_testing.md) | [Siguiente: LEGOs 🧱](../03_Clean_Code/03_guia_solid.md)
