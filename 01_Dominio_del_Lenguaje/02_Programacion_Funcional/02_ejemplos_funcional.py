from functools import reduce

# Datos de prueba: una lista de diccionarios (común en web/data)
usuarios = [
    {"nombre": "Ana", "edad": 25, "rol": "admin"},
    {"nombre": "Bob", "edad": 17, "rol": "user"},
    {"nombre": "Carlos", "edad": 30, "rol": "user"},
    {"nombre": "Diana", "edad": 19, "rol": "admin"},
]

print("--- 1. Lambda & Sorting ---")
# Ordenar por edad usando lambda
usuarios_ordenados = sorted(usuarios, key=lambda u: u["edad"])
print(f"Ordenados por edad: {[u['nombre'] for u in usuarios_ordenados]}")

print("\n--- 2. Filter & Map (Estilo Clásico) ---")
# Objetivo: Obtener nombres de usuarios mayores de edad (>=18) en mayúsculas

# Paso 1: Filtrar
adultos_iter = filter(lambda u: u["edad"] >= 18, usuarios)
# Paso 2: Map (Transformar a nombre mayúscula)
nombres_adultos_iter = map(lambda u: u["nombre"].upper(), adultos_iter)

print(f"Adultos (Map/Filter): {list(nombres_adultos_iter)}")

print("\n--- 3. List Comprehensions (Estilo Pythonico) ---")
# Lo mismo pero más legible
nombres_adultos_comp = [
    u["nombre"].upper() 
    for u in usuarios 
    if u["edad"] >= 18
]
print(f"Adultos (Comprehension): {nombres_adultos_comp}")

print("\n--- 4. Reduce ---")
# Objetivo: Sumar todas las edades
total_edad = reduce(lambda acc, u: acc + u["edad"], usuarios, 0)
print(f"Suma de edades: {total_edad}")

print("\n--- 5. Dict Comprehension ---")
# Crear un diccionario nombre: rol
mapa_roles = {u["nombre"]: u["rol"] for u in usuarios}
print(f"Mapa de roles: {mapa_roles}")
