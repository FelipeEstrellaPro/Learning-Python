# ⏱️ Profiling: El Velocímetro

![Difficulty](https://img.shields.io/badge/Dificultad-Experto-red)

## 👶 Explicación para Niños (ELI5)

Tu auto de carreras va lento. 🐢
¿Qué está fallando? ¿El motor? ¿Las ruedas? ¿O es que llevas el freno de mano puesto?
**Profiling** es ponerle sensores al auto para ver exactamente qué pieza está tardando más.
No adivines. **Mide**.

## 🛠️ Herramientas de Medición

### 1. `timeit` (El Cronómetro)
Para carreras cortas. Mide cuánto tarda una sola línea de código repetida muchas veces.
Ideal para saber si es más rápido `list()` o `[]`.

### 2. `cProfile` (El Escáner Completo)
Te da un reporte detallado de TODAS las funciones que se ejecutaron.
- ¿Cuántas veces se llamó a `calcular()`?
- ¿Cuánto tiempo total pasó ahí?

## 🕵️‍♂️ Detective de Cuellos de Botella

Un "Cuello de Botella" (Bottleneck) es esa parte pequeña del código que frena todo lo demás.
Regla de Pareto (80/20):
El 80% del tiempo de tu programa se gasta en el 20% del código.
**Encuentra ese 20% y arréglalo.**

---
[⬅️ Anterior: Etiquetadora](../03_Tipado/03_guia_type_hinting.md) | [Subir de Nivel: Ingeniería 🏭](../../03_Ingenieria_Software/README.md)
