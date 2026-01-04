# Type Hinting: Python Moderno y Robusto

## 1. ¿Por qué Tipar?
Python es dinámico, pero el tipado opcional ("Type Hints") introducido en PEP 484 permite:
- **Autocompletado IDE**: Mucho más inteligente y preciso.
- **Reducción de Bugs**: Herramientas como `mypy` detectan errores de tipo antes de ejecutar.
- **Documentación**: El código se explica solo.

## 2. Tipos Básicos y `typing`

Desde Python 3.9+, puedes usar tipos nativos `list`, `dict`, `set` en lugar de importar `List` de `typing`.

```python
# Antes (3.8-)
from typing import List
def procesar(items: List[int]) -> None: ...

# Ahora (3.9+)
def procesar(items: list[int]) -> None: ...
```

### Tipos Comunes
- `Optional[int]`: Puede ser `int` o `None`. (También `int | None` en 3.10+).
- `Union[int, str]`: Puede ser entero o string. (También `int | str` en 3.10+).
- `Any`: Desactiva el chequeo de tipos (evítalo si puedes).
- `Callable[[int, int], str]`: Una función que recibe dos enteros y devuelve string.

## 3. Avanzado: Generics y Protocolos

### Generics (`TypeVar`)
Para funciones que funcionan con varios tipos pero mantienen la relación entre ellos.
`T = TypeVar('T')`

### Protocol (`Duck Typing` Tipado)
Define "qué métodos debe tener" un objeto, sin importar de qué clase herede. Es la versión formal del Duck Typing.

## 4. Análisis Estático
Instala `mypy` y corre:
`mypy mi_archivo.py`
Te avisará si intentas sumar un string a un entero, etc.
