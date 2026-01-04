# 🏗️ POO Avanzada: El Plano Maestro

![Difficulty](https://img.shields.io/badge/Dificultad-Dificil-red)

## 👶 Explicación para Niños (ELI5)

Imagina que eres un arquitecto.
- **Clase (`class`)**: Es el **PLANO**. Dibujas una casa en un papel. No puedes vivir en el papel.
- **Objeto (`instance`)**: Es la **CASA REAL**. Usas el plano para construir 100 casas iguales en la calle.

### ¿Qué son los "Mixins"? 🧩
Imagina que quieres que algunas casas tengan piscina y otras tengan alarma.
En lugar de dibujar un plano nuevo entero, tienes un "Sticker de Piscina" y un "Sticker de Alarma".
Simplemente le pegas el sticker al plano y ¡Pum! La casa tiene piscina. Eso es un **Mixin**.

---

## 🪄 Hechizos Mágicos (Dunder Methods)

Python te deja hacer trucos si usas nombres especiales con doble guion bajo `__`.

| Hechizo | ¿Qué hace? | Ejemplo |
| :--- | :--- | :--- |
| `__init__` | El conjuro de nacimiento. | Cuando nace la casa, píntala de azul. |
| `__str__` | El nombre público. | Si le pregunto "¿Quién eres?", me dice "Casa Azul". |
| `__add__` | Fusión. | Si sumo Casa A + Casa B, obtengo una Mansión. |

> [!CAUTION]
> **Properties (`@property`)**:
> Sirven para poner un guardia de seguridad en tu casa.
> Si alguien intenta decir `casa.precio = -50`, el guardia (el `setter`) le grita: "¡El precio no puede ser negativo!" 👮‍♂️

---
[⬅️ Anterior: Fábrica](../02_Programacion_Funcional/02_guia_funcional.md) | [Siguiente: Regalos ➡️](../04_Decoradores_Generadores/04_guia_deco_gen.md)
