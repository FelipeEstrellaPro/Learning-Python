# 🏭 Programación Funcional: La Fábrica de Juguetes

![Difficulty](https://img.shields.io/badge/Dificultad-Media-yellow)

## 👶 Explicación para Niños (ELI5)

Imagina una fábrica de autos.
1.  Entra una pieza de metal.
2.  Un robot la aplasta (**Map**).
3.  Otro robot revisa si está rota (**Filter**).
4.  Al final se juntan todas las piezas (**Reduce**).

En Python, tus datos son las piezas de metal y las "Funciones" son los robots.
Lo genial es que **los robots no guardan las piezas**, solo las pasan al siguiente.

---

## 🛠️ Los 3 Robots Maestros

### 1. El Robot Transformador (`map`)
Toma un carrito y lo pinta de rojo.
`map(pintar_rojo, lista_de_autos)`

### 2. El Robot Inspector (`filter`)
Deja pasar solo a los autos que tienen 4 ruedas. Los de 3 ruedas se van a la basura.
`filter(tiene_4_ruedas, lista_de_autos)`

### 3. El Robot Empaquetador (`reduce`)
Toma todos los autos y los mete en un camión gigante (un solo resultado).
`reduce(sumar, lista_numeros)`

> [!TIP]
> **Comprensiones (La Magia)**:
> Python tiene una forma secreta de escribir esto más rápido. Se llaman "List Comprehensions".
> Es como decirle a la fábrica: *"¡Hazme una lista de autos rojos que tengan 4 ruedas!"* en una sola frase.
> `[pintar(auto) for auto in autos if tiene_4_ruedas(auto)]`

---
[⬅️ Anterior: Mochila Mágica](../01_Estructuras_de_Datos/01_guia_estructuras.md) | [Siguiente: Planos Maestros ➡️](../03_POO/03_guia_poo.md)
