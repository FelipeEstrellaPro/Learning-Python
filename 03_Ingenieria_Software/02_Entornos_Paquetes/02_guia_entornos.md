# 📦 Entornos y Paquetes

![Level 3](https://img.shields.io/badge/Level-3-green)

## 1. El Caos de las Dependencias 🔥
Instalar todo con `pip install X` en tu sistema global es receta para el desastre ("Dependency Hell").

> [!IMPORTANT]
> **Regla de Oro**: Cada proyecto debe tener su propio entorno aislado.

## 2. Herramientas Modernas

### `venv` (Estándar) 🐢
- Viene con Python.
- `python -m venv .venv`
- Bueno para scripts simples, requiere gestión manual de `requirements.txt`.

### `Poetry` (El Estándar Profesional) 🎩
Combina gestión de dependencias, empaquetado y publicación.
- Usa `pyproject.toml` (estándar PEP 518).
- Resuelve conflictos de versiones ("Lockfile").
- Comandos: `poetry add numpy`, `poetry shell`.

## 3. pyproject.toml 📄
El archivo único para gobernar todo. Reemplaza a `setup.py`, `requirements.txt`, `pytest.ini`, etc.

```toml
[tool.poetry]
name = "mi-proyecto"
version = "0.1.0"
description = ""
authors = ["Tu Nombre <tu@email.com>"]

[tool.poetry.dependencies]
python = "^3.10"
requests = "^2.28.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

---
[⬅️ Anterior: Testing](../01_Testing/01_guia_testing.md) | [Siguiente: Clean Code 🧹](../03_Clean_Code/03_guia_solid.md)
