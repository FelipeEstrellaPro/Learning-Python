# Programación Funcional en Python

## 1. ¿Qué es?
Python no es un lenguaje puramente funcional (como Haskell), pero soporta muchas características funcionales. Esto significa tratar a las funciones como ciudadanos de primera clase (pueden pasarse como argumentos, retornarse, asignarse a variables).

## 2. Herramientas Principales

### 2.1 Lambda (Funciones Anónimas)
Funciones pequeñas, de una sola línea, sin nombre.
`lambda argumentos: expresion`
> **Uso común**: Como argumento para `sort`, `max`, `min` o `map`.

### 2.2 Map, Filter, Reduce
- **Map(func, iterable)**: Aplica `func` a cada elemento. Retorna un iterador.
- **Filter(func, iterable)**: Retorna elementos donde `func` es True.
- **Reduce(func, iterable)**: Aplica `func` acumulativamente (requiere `functools`).

### 2.3 Comprensiones (Comprehensions)
La forma "Pythonica" de hacer map/filter. Son más legibles y, a menudo, más rápidas.

- **List Comprehension**: `[x*2 for x in lista if x > 0]`
- **Dict Comprehension**: `{k:v for k,v in lista}`
- **Set Comprehension**: `{x for x in lista}`

## 3. ¿Map/Filter o Comprehensions?
En Python, **casi siempre se prefieren las comprensiones** por legibilidad.
`map` y `filter` pueden ser útiles si ya tienes la función definida o si necesitas "lazy evaluation" (aunque las expresiones generadoras también lo hacen).

## 4. Diagrama: Flujo de Datos

```mermaid
graph LR
    A[Datos Entrada] --> B{Filter}
    B -- Cumple condición --> C[Map (Transformar)]
    C --> D[Reduce (Agregar)]
    D --> E[Resultado Final]
```
