import timeit
import collections
import sys

def separador(titulo):
    print(f"\n{'='*50}")
    print(f" {titulo}")
    print(f"{'='*50}")

# ---------------------------------------------------------
# 1. Rendimiento: List vs Set (Búsqueda)
# ---------------------------------------------------------
separador("1. Rendimiento: List vs Set")

# Creamos una lista y un set con 1 millón de números
N = 1_000_000
mi_lista = list(range(N))
mi_set = set(range(N))

# Elemento a buscar (el último, peor caso para lista)
target = N - 1

def buscar_en_lista():
    return target in mi_lista

def buscar_en_set():
    return target in mi_set

tiempo_lista = timeit.timeit(buscar_en_lista, number=1000)
tiempo_set = timeit.timeit(buscar_en_set, number=1000)

print(f"Búsqueda 1000 veces del elemento {target} en {N} elementos:")
print(f"Lista (O(n)): {tiempo_lista:.6f} segundos")
print(f"Set   (O(1)): {tiempo_set:.6f} segundos")
print(f"El set es {tiempo_lista/tiempo_set:.2f} veces más rápido aquí.")

# ---------------------------------------------------------
# 2. Collections: Deque vs List (Pop(0))
# ---------------------------------------------------------
separador("2. Collections: Deque para Colas")

# Simulamos una cola
mi_deque = collections.deque(range(100_000))
mi_lista_cola = list(range(100_000))

def pop_lista():
    if mi_lista_cola:
        mi_lista_cola.pop(0) # O(n) - debe mover todo el resto

def pop_deque():
    if mi_deque:
        mi_deque.popleft() # O(1)

tiempo_pop_lista = timeit.timeit(pop_lista, number=1000)
tiempo_pop_deque = timeit.timeit(pop_deque, number=1000)

print(f"Eliminar 1000 elementos al inicio (FIFO):")
print(f"Lista (pop(0)): {tiempo_pop_lista:.6f} s")
print(f"Deque (popleft): {tiempo_pop_deque:.6f} s")

# ---------------------------------------------------------
# 3. Collections: Counter
# ---------------------------------------------------------
separador("3. Collections: Counter")

texto = "python es genial python es rapido python es vida"
palabras = texto.split()
contador = collections.Counter(palabras)

print(f"Texto: {texto}")
print(f"Conteo: {contador}")
print(f"Top 2 más comunes: {contador.most_common(2)}")

# ---------------------------------------------------------
# 4. Collections: Defaultdict
# ---------------------------------------------------------
separador("4. Collections: Defaultdict")

# Caso: Agrupar palabras por su longitud
palabras_lista = ["hola", "sol", "cielo", "mar", "luna", "día"]
agrupacion = collections.defaultdict(list)

for p in palabras_lista:
    agrupacion[len(p)].append(p)

print(f"Palabras agrupadas por longitud: {dict(agrupacion)}")
# Sin defaultdict tendríamos que hacer: if len(p) not in d: d[len(p)] = [] ...

