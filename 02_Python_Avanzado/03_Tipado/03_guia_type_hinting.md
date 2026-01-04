# 🏷️ Tipado: La Etiquetadora

![Difficulty](https://img.shields.io/badge/Dificultad-Facil-green)

## 👶 Explicación para Niños (ELI5)

Python es un lenguaje "relajado".
Puedes meter un gato en una caja de zapatos. 📦🐈
Pero si luego intentas ponerte los zapatos... ¡Miau! 🩸 (Error en tiempo de ejecución).

**Type Hinting** es usar una etiquetadora para poner un cartel en la caja: "SOLO ZAPATOS".
Si intentas meter al gato, una alarma suena antes de que siquiera abras la caja (Mypy).

---

## 🦆 El Pato Espacial (Protocol y Duck Typing)

En Python decimos: *"Si camina como pato y hace cuac, es un pato"*.
Pero a veces necesitas ser más formal.
**Protocol** es un contrato.
*"No me importa qué animal seas, pero firma aquí que prometes saber Volar"*.

```python
class Volador(Protocol):
    def volar(self): ...

def lanzar_al_vacio(x: Volador):
    x.volar()
```
Ahora el editor (VS Code) te avisará si intentas lanzar al vacío a un Elefante que no sabe volar. 🐘🚫

---
[⬅️ Anterior: Limpieza](../02_Gestion_Memoria/02_guia_memoria.md) | [Siguiente: Velocímetro ⏱️](../04_Profiling/04_guia_profiling.md)
