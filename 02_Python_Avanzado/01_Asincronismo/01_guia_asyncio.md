# ⏳ Asincronismo: El Chef Multitarea

![Difficulty](https://img.shields.io/badge/Dificultad-Experto-red)

## 👶 Explicación para Niños (ELI5)

Imagina una cocina. 👨‍🍳
- **Síncrono (Normal)**: Pones agua a hervir (tarda 10 min) y te quedas mirando la olla sin hacer nada hasta que hierva. Luego cortas la cebolla. 🐢
- **Asíncrono (`asyncio`)**: Pones el agua, y **mientras hierve**, cortas la cebolla, lavas los platos y bailas. Cuando el agua pita, vuelves a la olla. ⚡

## 🎡 El Event Loop (La Rueda de la Fortuna)
Es el jefe de cocina. Tiene una lista de tareas.
1.  "Agua hirviendo... esperar".
2.  "Cebolla... cortar".
El jefe va rotando rapidísimo viendo qué tarea ya se puede avanzar.

---

## 🚦 Semáforos y Reglas

### `async def` y `await`
- `async def cocinar()`: Define una tarea que puede pausarse.
- `await hervir_agua()`: Significa "Pausa esto, ve a hacer otra cosa útil y avísame cuando el agua esté lista".

> [!CAUTION]
> **El GIL (Un solo cocinero)**:
> Python solo tiene **UN** cocinero (un hilo de CPU).
> Asyncio sirve para cuando el cocinero tiene que ESPERAR cosas externas (horno, delivery, base de datos).
> Si le pides al cocinero picar 1 millón de cebollas (cálculo matemático), se bloqueará igual. Para eso necesitas `multiprocessing` (contratar más cocineros).

---
[⬅️ Volver a Pits](../README.md) | [Siguiente: Limpieza 🧹](../02_Gestion_Memoria/02_guia_memoria.md)
