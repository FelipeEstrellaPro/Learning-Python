# 🧠 Gestión de Memoria: El Equipo de Limpieza

![Difficulty](https://img.shields.io/badge/Dificultad-Media-yellow)

## 👶 Explicación para Niños (ELI5)

Tu programa es una fiesta. 🎉
Los invitados son las variables y datos.
La memoria RAM es la casa. Si entra demasiada gente, la casa explota (Crash).

En Python, tienes un **Mayordomo Automático** (Garbage Collector).
- Cuando un invitado se queda solo en un rincón y nadie le habla (Contador de Referencias = 0), el mayordomo lo echa de la casa. 👋

---

## 📉 Trucos para Ahorrar Espacio

### `__slots__` (Sillas Reservadas)
Por defecto, cada invitado (Objeto) trae una mochila gigante vacía (`__dict__`) por si quiere guardar cosas nuevas. Eso ocupa mucho espacio.
Si usas `__slots__ = ['nombre']`, le dices: *"Solo puedes traer tu nombre, nada de mochilas"*.
**Resultado**: Caben el doble de invitados en la misma casa.

### El Mito de los Hilos (Threading) 🧵
Mucha gente cree que usar hilos (`threading`) hace que Python piense más rápido.
**FALSO**.
Por culpa de un candado llamado **GIL**, solo un hilo puede "pensar" a la vez.
Los hilos solo sirven si uno se duerme (esperando red), para que el otro trabaje.

---
[⬅️ Anterior: Chef Multitarea](../01_Asincronismo/01_guia_asyncio.md) | [Siguiente: Etiquetadora 🏷️](../03_Tipado/03_guia_type_hinting.md)
