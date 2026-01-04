# 📊 Data Science: El Analista Pokémon

![Difficulty](https://img.shields.io/badge/Dificultad-Analitica-orange)
![Reading Time](https://img.shields.io/badge/Lectura-12_min-blue)

## 👶 1. Explicación para Niños (ELI5)

Imagina una hoja de Excel gigante con los 800 Pokémon. 🐲
Si quieres saber "¿Cuál es el tipo más fuerte?", tardarías días contando a mano.
Con **Pandas**, es como tener un asistente superinteligente. Le dices: "Filtra los de Fuego y saca el promedio de Ataque", y ¡ZAS! Te da la respuesta en 0.1 segundos.

---

## 🔬 2. Deep Dive: Vectorización

¿Por qué `numpy` y `pandas` son rápidos?
Porque no usan bucles `for` de Python (que son lentos).
Usan **Instrucciones Vectoriales (SIMD)** en C.
Le dicen al Procesador: "Multiplica estos 1000 números por 2 A LA VEZ", en lugar de uno por uno.

---

## 📊 3. Visualización: DataFrame vs Spreadsheet

```mermaid
graph TD
    subgraph Raw Data [CSV File]
        Rows[Fila 1...1000]
    end
    
    subgraph Pandas [DataFrame en RAM]
        Index[Indice (Pikachu, Charmander...)]
        Col1[Columna: Ataque (Int64 Array)]
        Col2[Columna: Tipo (Category)]
        
        Index -- O(1) Access --> Col1
    end
    
    Raw Data -- read_csv() --> Pandas
    Pandas -- plot() --> Grafico[Gráfico Bonito]
```

---

## 👩‍💻 4. Tutorial Interactivo: Analizando Pokémon

Necesitas: `pip install pandas`

```python
import pandas as pd

# 1. CREAMOS DATOS (Normalmente vendrían de un CSV)
data = {
    'Nombre': ['Pikachu', 'Charmander', 'Squirtle', 'Bulbasaur', 'Charizard', 'Mewtwo'],
    'Tipo': ['Eléctrico', 'Fuego', 'Agua', 'Planta', 'Fuego', 'Psíquico'],
    'HP': [35, 39, 44, 45, 78, 106],
    'Ataque': [55, 52, 48, 49, 84, 110],
    'Legendario': [False, False, False, False, False, True]
}

df = pd.DataFrame(data)

print("--- 📋 LOS DATOS ---")
print(df)

# 2. FILTRADO (Querying)
print("\n--- 🔥 SOLO FUEGO ---")
fuego = df[df['Tipo'] == 'Fuego']
print(fuego[['Nombre', 'Ataque']])

# 3. ESTADÍSTICAS (Aggregation)
print("\n--- 🥊 PROMEDIO DE ATAQUE POR TIPO ---")
# Agrupar por 'Tipo' y calcular la media de 'Ataque'
ranking = df.groupby('Tipo')['Ataque'].mean().sort_values(ascending=False)
print(ranking)

# 4. CREAR NUEVAS COLUMNAS (Feature Engineering)
# Poder Total = HP + Ataque
df['Poder_Total'] = df['HP'] + df['Ataque']
mas_fuerte = df.loc[df['Poder_Total'].idxmax()]

print(f"\n🏆 EL CAMPEÓN ES: {mas_fuerte['Nombre']} ({mas_fuerte['Poder_Total']} puntos)")
```

### 🧠 ¿Qué aprendimos?
1.  **DataFrame**: Es la estructura central. Filas y Columnas con superpoderes.
2.  **`groupby`**: La herramienta más potente. "Parte los datos en grupos, aplica una fórmula a cada grupo, y combina los resultados".
3.  **Vectorización**: `df['HP'] + df['Ataque']` suma toda la columna de una vez. No hace falta un bucle.

---
[⬅️ Anterior: Web API](../01_Web/01_guia_web.md) | [Siguiente: Automatización 🤖](../03_DevOps/03_guia_devops.md)
