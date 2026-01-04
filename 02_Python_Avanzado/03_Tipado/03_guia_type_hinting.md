# 🏷️ Tipado: La Etiquetadora

![Difficulty](https://img.shields.io/badge/Dificultad-Facil-green)
![Reading Time](https://img.shields.io/badge/Lectura-8_min-blue)

## 👶 1. Explicación para Niños (ELI5)

Python es un lenguaje "relajado".
Puedes meter un gato en una caja de zapatos. 📦🐈
Pero si luego intentas ponerte los zapatos... ¡Miau! 🩸 (Error en tiempo de ejecución).

**Type Hinting** es usar una etiquetadora para poner un cartel en la caja: "SOLO ZAPATOS".
Si intentas meter al gato, una alarma suena antes de que siquiera abras la caja (VS Code / Mypy).

---

## 🔬 2. Deep Dive: Tipado Gradual

Python no se convirtió en Java.
El tipado es **Opcional** y **Ignorado en Runtime**.
- Si escribes `x: int = "hola"`, el programa correrá igual (y fallará después).
- Los Type Hints son para los humanos y para las máquinas de análisis estático (Linters).

---

## 📊 3. Visualización: Antes y Después

```mermaid
graph TD
    subgraph Caos [Sin Tipado]
        A[func(a, b)] --> B{¿Qué es a?}
        B -- ??? --> C[Leer Documentación]
        C -- No hay docs --> D[Leer Código Entero]
        D -- Dolor de cabeza --> E[Adivinar]
    end
    
    subgraph Orden [Con Tipado]
        F[func(a: int, b: str)] --> G[IDE Autocompleta]
        G --> H[Productividad 🚀]
    end
```

---

## 👩‍💻 4. Tutorial Interactivo: Duck Typing Formal (Protocol)

En POO clásica, usas Herencia para definir tipos. En Python moderno, usas **Estructura**.

```python
from typing import Protocol, List

# 1. DEFINIMOS EL PROTOCOLO (La Forma)
class Comible(Protocol):
    """Cualquier cosa que tenga un método morder()"""
    def morder(self) -> str:
        ...

# 2. DEFINIMOS CLASES DISPARES
class Manzana:
    def morder(self) -> str:
        return "Crunch! 🍎"

class Pan:
    def morder(self) -> str:
        return "Ñam! 🥖"

class Piedra:
    # La piedra NO tiene método morder()
    pass

# 3. FUNCIÓN QUE EXIGE EL PROTOCOLO
def comer_algo(alimento: Comible):
    print(f"Comiendo: {alimento.morder()}")

# 4. PRUEBA
m = Manzana()
p = Pan()
r = Piedra()

comer_algo(m) # ✅ OK: Manzana es Comible
comer_algo(p) # ✅ OK: Pan es Comible

# comer_algo(r) 
# 🚩 SI TUVIESES MYPY INSTALADO, AQUÍ SALDRÍA ERROR ROJO: 
# "Argument 1 to 'comer_algo' has incompatible type 'Piedra'; expected 'Comible'"
```

### 🧠 ¿Qué aprendimos?
1.  **Inversión de Control**: `Manzana` no necesita saber que existe `Comible`. No hay herencia (`class Manzana(Comible)` NO es necesario).
2.  **Seguridad**: Validamos que los objetos cumplan contratos sin perder la flexibilidad de Python.

---
[⬅️ Anterior: Limpieza](../02_Gestion_Memoria/02_guia_memoria.md) | [Siguiente: Velocímetro ⏱️](../04_Profiling/04_guia_profiling.md)
