# 🧠 Gestión de Memoria: El Equipo de Limpieza

![Difficulty](https://img.shields.io/badge/Dificultad-Media-yellow)
![Reading Time](https://img.shields.io/badge/Lectura-10_min-blue)

## 👶 1. Explicación para Niños (ELI5)

Tu programa es una fiesta. 🎉
Los invitados son las variables y datos.
La memoria RAM es la casa. Si entra demasiada gente, la casa explota (Crash).

En Python, tienes un **Mayordomo Automático** (Garbage Collector).
- Cuando un invitado se queda solo en un rincón y nadie le habla (Contador de Referencias = 0), el mayordomo lo echa de la casa. 👋

---

## 🔬 2. Deep Dive: PyObject y el Overhead

En C, un entero `int32` ocupa 4 bytes.
En Python, un `int` es un objeto complejo (`PyObject`) que contiene:
1.  **Reference Count**: ¿Cuántos variables me apuntan? (8 bytes)
2.  **Type Pointer**: ¿Qué soy? (Int) (8 bytes)
3.  **Value**: El valor real (e.g. 5) (8 bytes)
Total: ~28 bytes. ¡7 veces más grande!

Por eso Python consume mucha RAM.

---

## 📊 3. Visualización: Referencias Circulares

```mermaid
graph LR
    VarA[Variable A] --> ObjA((Objeto A))
    VarB[Variable B] --> ObjB((Objeto B))
    
    ObjA -- ref --> ObjB
    ObjB -- ref --> ObjA
    
    style ObjA fill:#ffcccc
    style ObjB fill:#ffcccc
    
    note right of ObjB: Ciclo de Referencia!\nEl RefCount nunca llega a 0.\nAquí entra el Garbage Collector (GC).
```

---

## 👩‍💻 4. Tutorial Interactivo: Ahorrando RAM con __slots__

Vamos a ver cómo optimizar una clase para que ocupe la mitad de memoria.

```python
import sys
from pympler import asizeof # Nota: library externa habitual, pero usaremos sys para demo base

# 1. CLASE NORMAL (Derrochadora)
class PixelNormal:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    # Internamente tiene un diccionario self.__dict__ = {'x': 1, ...}

# 2. CLASE OPTIMIZADA (Slots)
class PixelSlots:
    # Le decimos a Python: "NO crees un diccionario. Solo reserva espacio para x, y, z"
    __slots__ = ['x', 'y', 'z']
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# 3. MEDICIÓN
p1 = PixelNormal(10, 20, 30)
p2 = PixelSlots(10, 20, 30)

# getsizeof es básico y a veces engañoso, pero sirve para comparar el objeto base
size_normal = sys.getsizeof(p1) + sys.getsizeof(p1.__dict__) 
size_slots = sys.getsizeof(p2)

print(f"--- Comparación de Tamaño (Bytes aproximados) ---")
print(f"Normal: {size_normal} bytes")
print(f"Slots:  {size_slots} bytes")

factor = (1 - (size_slots / size_normal)) * 100
print(f"📉 Ahorro: {factor:.1f}% de memoria por objeto.")
print("\n¡Imagina esto multiplicado por 1 millón de pixeles en una imagen!")
```

### 🧠 ¿Qué aprendimos?
1.  **`__dict__`**: Es el culpable del consumo de memoria en objetos normales. Permite añadir atributos dinámicamente (`p1.nuevo = 5`), pero cuesta caro.
2.  **`__slots__`**: Mata el dinamismo (no puedes añadir atributos nuevos en runtime) a cambio de eficiencia pura.

---
[⬅️ Anterior: Chef Multitarea](../01_Asincronismo/01_guia_asyncio.md) | [Siguiente: Etiquetadora 🏷️](../03_Tipado/03_guia_type_hinting.md)
