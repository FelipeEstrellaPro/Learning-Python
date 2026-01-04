import time
import functools
import sys

# ---------------------------------------------------------
# 1. Decoradores
# ---------------------------------------------------------
def timer_decorator(func):
    """Mide el tiempo de ejecución de una función."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fin = time.perf_counter()
        print(f"[{func.__name__}] tardó {fin - inicio:.6f} segundos")
        return resultado
    return wrapper

@timer_decorator
def operacion_pesada(n):
    """Simula una carga de trabajo."""
    return sum(i**2 for i in range(n))

print("--- 1. Decorador en Acción ---")
res = operacion_pesada(1_000_000)
print(f"Resultado: {res}")
# Gracias a wraps, conservamos la metadata
print(f"Nombre función: {operacion_pesada.__name__}")

# ---------------------------------------------------------
# 2. Generadores (Yield)
# ---------------------------------------------------------
def fibonacci_gen(limit):
    """Generador infinito (o limitado) de Fibonacci."""
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

print("\n--- 2. Generador Manual (Yield) ---")
for num in fibonacci_gen(10):
    print(num, end=" ")
print()

# ---------------------------------------------------------
# 3. List vs Generator (Uso de Memoria)
# ---------------------------------------------------------
print("\n--- 3. Memoria: Lista vs Generador ---")
N = 1_000_000
# Lista: Crea todos los elementos en memoria
lista_comp = [x**2 for x in range(N)]
# Generador: No crea nada aún, solo guarda la "regla"
gen_exp = (x**2 for x in range(N))

size_lista = sys.getsizeof(lista_comp)
size_gen = sys.getsizeof(gen_exp)

print(f"Tamaño Lista ({N} elementos): {size_lista / 1024 / 1024:.2f} MB")
print(f"Tamaño Generador: {size_gen} Bytes (!!)")
print(f"Ahorro de memoria: {size_lista / size_gen:.0f}x veces menos")
