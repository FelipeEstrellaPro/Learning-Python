import pandas as pd
import numpy as np

print("--- 1. NumPy Vectorization ---")
# Crear lista vs array
lista = range(1_000_000)
arr = np.array(lista)

# Operación vectorizada (Rápido)
# No necesitamos "for x in arr"
arr_cuadrado = arr ** 2 
print(f"Último elemento al cuadrado: {arr_cuadrado[-1]}")

print("\n--- 2. Pandas DataFrame ---")
data = {
    "nombre": ["Ana", "Bob", "Charlie", "David"],
    "edad": [24, 17, 35, 29],
    "ciudad": ["Madrid", "Barcelona", "Madrid", "Valencia"]
}

df = pd.DataFrame(data)
print("DataFrame Original:")
print(df)

print("\n--- 3. Filtrado y Agregación ---")
# SQL: SELECT * FROM df WHERE edad >= 18
adultos = df[df["edad"] >= 18]
print(f"Adultos:\n{adultos}")

# SQL: SELECT ciudad, AVG(edad) FROM df GROUP BY ciudad
promedio_edad = df.groupby("ciudad")["edad"].mean()
print(f"\nEdad promedio por ciudad:\n{promedio_edad}")
