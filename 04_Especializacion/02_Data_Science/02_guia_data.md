# 📊 Data Science: Analista Pokémon

![Difficulty](https://img.shields.io/badge/Dificultad-Visual-blue)

## 👶 Explicación para Niños (ELI5)

Imagina que tienes una colección de 1,000 cartas Pokémon.
Quieres saber: **¿Son más fuertes los de Fuego o los de Agua?** 🔥 vs 💧

- **A mano**: Tardarías horas sumando ataque por ataque.
- **Con Pandas (`pandas`)**: Es como un Excel superpoderoso. Le dices: *"Agrupa por tipo y dame el promedio de ataque"*. ¡BOOM! Resultado en 0.01 segundos.

---

## 🐼 Pandas en Acción

Imagina que tus datos son una tabla gigante llamada `df` (DataFrame).

```python
# 1. ¿Quién es más fuerte?
fuego = df[df["Tipo"] == "Fuego"]
agua = df[df["Tipo"] == "Agua"]

print(fuego["Ataque"].mean()) # 78.5
print(agua["Ataque"].mean())  # 72.1
```
¡Conclusión científica! Los de fuego pegan más fuerte. (Datos inventados para el ejemplo, ¡compruébalo tú!).

---
[⬅️ Anterior: Pizzería](../01_Web/01_guia_web.md) | [Siguiente: Robot Mayordomo 🤖](../03_DevOps/03_guia_devops.md)
