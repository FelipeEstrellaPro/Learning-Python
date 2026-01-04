# Desarrollo Web Moderno: FastAPI

## 1. ¿Por qué FastAPI?
- **Velocidad**: Casi tan rápido como NodeJS/Go (gracias a Starlette y Pydantic).
- **Estándares**: Basado en JSON Schema y OpenAPI.
- **Productividad**: Autocompletado, menos errores, docs automáticos.

## 2. Componentes Clave

### Pydantic
Validación de datos usando Type Hints.
```python
class Item(BaseModel):
    nombre: str
    precio: float
```
Si mandas un string en `precio`, Pydantic lanza error automáticamente.

### OpenAPI (Swagger UI)
FastAPI genera `/docs` automáticamente. No necesitas escribir YAMLs gigantes a mano.

### Async Nativo
Defines endpoints con `async def`, permitiendo alta concurrencia.
