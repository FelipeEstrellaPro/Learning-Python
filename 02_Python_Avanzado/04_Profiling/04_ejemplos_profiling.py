import cProfile
import pstats
import time
import random

def funcion_lenta():
    """Simula una función pesada: Sumar números inútilmente."""
    total = 0
    # Cuello de botella aquí: bucle gigante
    for _ in range(2_000_000):
        total += random.random()
    return total

def funcion_rapida():
    """Simula una función optimizada."""
    return sum([1 for _ in range(1000)])

def main():
    print("🏎️ Iniciando carrera...")
    funcion_lenta()
    funcion_lenta()
    funcion_rapida()
    print("🏁 Carrera terminada.")

if __name__ == "__main__":
    # Opción 1: Correr cProfile directamente en el código
    print("--- 📊 Reporte de Profiling ---")
    profiler = cProfile.Profile()
    profiler.enable()
    
    main()
    
    profiler.disable()
    
    # Ordenar resultados por tiempo acumulado (cumtime)
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats(10) # Mostrar top 10 funciones más lentas
    
    print("\n💡 TIP: Mira arriba. 'funcion_lenta' debería tener el mayor 'cumtime'.")
