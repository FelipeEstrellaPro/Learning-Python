# Gestión de Memoria y Rendimiento

## 1. El GIL (Global Interpreter Lock)
El GIL es un semáforo que asegura que solo un hilo de ejecución (thread) corra a la vez en el intérprete de CPython.
- **Consecuencia**: `threading` no sirve para paralelismo real de CPU (cálculos matemáticos). Solo sirve para I/O.
- **Solución**: Para usar todos los núcleos del CPU, usa `multiprocessing`.

## 2. Administración de Memoria
Python gestiona la memoria automáticamente, pero entender cómo funciona ayuda a optimizar.

### Reference Counting (Conteo de Referencias)
Es el mecanismo principal. Cada objeto tiene un contador. Si llega a 0, se elimina inmediatamente.
`sys.getrefcount(obj)`

### Garbage Collector (GC)
Mecanismo secundario para detectar **ciclos de referencia** (A apunta a B y B apunta a A). Se ejecuta periódicamente.

## 3. Optimizaciones

### `__slots__`
Por defecto, las clases guardan atributos en un `dict` (`__dict__`), lo cual consume mucha RAM.
Si defines `__slots__ = ['nombre', 'edad']`, Python reserva espacio fijo y **no** crea el diccionario, ahorrando hasta un 40-50% de memoria en millones de objetos.

### Generadores vs Listas
(Visto en Nivel 1) Siempre prefiere generadores para secuencias largas.

## 4. Multiprocessing vs Threading

| Característica | Threading | Multiprocessing |
| :--- | :--- | :--- |
| **Memoria** | Compartida (Ligero) | Separada (Pesado) |
| **GIL** | Limitado por GIL | Evita el GIL |
| **Uso Ideal** | I/O Bound (Red, Disco) | CPU Bound (Cálculos) |
