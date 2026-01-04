import sys
import timeit

# ---------------------------------------------------------
# 1. Reference Counting
# ---------------------------------------------------------
print("--- 1. Reference Counting ---")
a = [1, 2, 3]
# El conteo es 2: la variable 'a' + el argumento pasado a getrefcount
print(f"Referencias de 'a': {sys.getrefcount(a)}")
b = a
print(f"Referencias tras 'b = a': {sys.getrefcount(a)}")
del b
print(f"Referencias tras 'del b': {sys.getrefcount(a)}")

# ---------------------------------------------------------
# 2. SLOTS vs DICT (Ahorro de Memoria)
# ---------------------------------------------------------
class ClaseNormal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class ClaseSlots:
    # Define atributos fijos, evita creación de __dict__
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

print("\n--- 2. Slots vs Dict ---")
obj_normal = ClaseNormal(10, 20)
obj_slots = ClaseSlots(10, 20)

# Tamaño del objeto en sí (sin contar el tamaño de los atributos referenciados)
size_normal = sys.getsizeof(obj_normal) + sys.getsizeof(obj_normal.__dict__)
size_slots = sys.getsizeof(obj_slots) 
# Nota: getsizeof es aproximado y shallow, pero ilustra el punto overhead.

print(f"Tamaño instancia Normal + dict: ~{size_normal} bytes")
print(f"Tamaño instancia Slots: {size_slots} bytes")
print("Nota: En millones de instancias, este ahorro es masivo.")

# ---------------------------------------------------------
# 3. Prueba rápida de creación (Slots suele ser más rápido)
# ---------------------------------------------------------
def crear_normales():
    return [ClaseNormal(i, i) for i in range(1000)]

def crear_slots():
    return [ClaseSlots(i, i) for i in range(1000)]

t_normal = timeit.timeit(crear_normales, number=100)
t_slots = timeit.timeit(crear_slots, number=100)

print(f"\nCreación de 100k objetos:")
print(f"Normal: {t_normal:.4f} s")
print(f"Slots:  {t_slots:.4f} s ({(t_normal/t_slots):.2f}x más rápido)")
