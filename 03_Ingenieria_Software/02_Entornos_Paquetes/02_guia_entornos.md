# Entornos y Paquetes

## 1. El Caos de las Dependencias
Instalar todo con `pip install X` en tu sistema global es receta para el desastre ("Dependency Hell").
**Regla de Oro**: Cada proyecto debe tener su propio entorno aislado.

## 2. Herramientas Modernas

### `venv` (Estándar)
- Viene con Python.
- `python -m venv .venv`
- Bueno para scripts simples, requiere gestión manual de `requirements.txt`.

### `Poetry` (El Estándar Profesional)
Combina gestión de dependencias, empaquetado y publicación.
- Usa `pyproject.toml` (estándar PEP 518).
- Resuelve conflictos de versiones ("Lockfile").
- Comandos: `poetry add numpy`, `poetry shell`.

## 3. pyproject.toml
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
