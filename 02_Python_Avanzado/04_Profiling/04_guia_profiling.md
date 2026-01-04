# ⏱️ Profiling: El Velocímetro

![Difficulty](https://img.shields.io/badge/Dificultad-Experto-red)
![Reading Time](https://img.shields.io/badge/Lectura-10_min-blue)

## 👶 1. Explicación para Niños (ELI5)

Tu auto de carreras va lento. 🐢
¿Qué está fallando? ¿El motor? ¿Las ruedas? ¿O es que llevas el freno de mano puesto?
**Profiling** es ponerle sensores al auto para ver exactamente qué pieza está tardando más.
No adivines. **Mide**.

---

## 🔬 2. Deep Dive: Deterministic Profiling

Los profilers estadísticos miran el CPU cada X milisegundos.
`cProfile` es **Determinístico**: Captura CADA llamada a función, CADA retorno y CADA excepción.
- **Ventaja**: Precisión absoluta.
- **Desventaja**: Hace el programa un poco más lento (overhead), pero el ratio relativo de tiempo se mantiene.

---

## 📊 3. Visualización: El Gráfico de Llamadas

```mermaid
graph TD
    Main["Main 100%"] --> A["Carga Datos 10%"]
    Main --> B["Proceso Pesado 85%"]
    Main --> C["Guardar 5%"]
    
    B --> B1["Cálculo Matriz 5%"]
    B --> B2["Bucle For Mal Optimizado 80%"]
    
    style B2 fill:#ff3333,color:#fff
    note right of B2: "🔥 CUELLO DE BOTELLA HERE 🔥"
```

---

## 👩‍💻 4. Tutorial Interactivo: Encontrando al Culpable

Vamos a crear un programa con una función intencionalmente lenta y usar `cProfile` para descubrirla.

```python
import cProfile
import pstats
import time
import random

# --- CÓDIGO SOSPECHOSO ---
def funcion_rapida():
    return [x*2 for x in range(10000)]

def funcion_lenta():
    """Simula una función mal escrita que quema CPU"""
    total = 0
    # Este bucle es ineficiente a propósito
    for _ in range(500_000):
        total += random.random()
    return total

def main():
    print("🎬 Iniciando simulación...")
    for _ in range(5):
        funcion_rapida()
        funcion_lenta() # El culpable se esconde aquí

# --- ANÁLISIS FORENSE ---
if __name__ == "__main__":
    print("🕵️‍♂️ Ejecutando Profiler...")
    
    # 1. Creamos el profiler
    profiler = cProfile.Profile()
    
    # 2. Encendemos la grabadora
    profiler.enable()
    
    # 3. Corremos el programa sospechoso
    main()
    
    # 4. Apagamos
    profiler.disable()
    
    # 5. Imprimimos el reporte ordenado por tiempo acumulado (cumtime)
    print("\n--- 📉 REPORTE DE DAÑOS ---")
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    
    # Mostramos solo las 5 funciones que más tiempo tomaron
    stats.print_stats(5)
```

### 🧠 Cómo leer el reporte
- **ncalls**: Número de veces que se llamó la función. (e.g., 5 veces para `funcion_lenta`).
- **tottime**: Tiempo gastado EN la función (excluyendo sub-llamadas).
- **cumtime (Cumulative)**: Tiempo gastado en la función Y en todo lo que ella llamó. **Este es el dato clave**.
- Verás que `funcion_lenta` está arriba del todo. ¡Culpable atrapado! 👮

---
[⬅️ Anterior: Etiquetadora](../03_Tipado/03_guia_type_hinting.md) | [Subir de Nivel: Ingeniería 🏭](../../03_Ingenieria_Software/README.md)
