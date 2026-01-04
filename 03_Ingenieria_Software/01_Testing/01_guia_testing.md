# 🕵️‍♂️ Testing: El Inspector de Calidad

![Difficulty](https://img.shields.io/badge/Dificultad-Esencial-green)

## 👶 Explicación para Niños (ELI5)

Imagina que construyes un robot. 🤖
Antes de venderlo, tienes que probar si funciona.
- **Manual**: Lo enciendes y ves si camina. (Lento y aburrido).
- **Automático (`pytest`)**: Contratas a un ejército de mini-robots inspectores que revisan cada tornillo en 1 segundo.

## 🧪 Herramientas del Inspector

### 1. `assert` (El Detector de Mentiras)
Es una pregunta simple: *"¿Es esto verdad?"*.
```python
def sumar(a, b): return a + b

# El test
def test_suma():
    resultado = sumar(2, 2)
    assert resultado == 4  # ✅ Pasa
    assert resultado == 5  # ❌ Falla y suena la alarma 🚨
```

### 2. Fixtures (El Ayudante de Escenario)
Imagina que para probar el robot necesitas construir una ciudad de cartón.
En lugar de construirla en CADA test, usas un **Fixture**.
El ayudante construye la ciudad, tú pruebas el robot, y el ayudante destruye la ciudad al terminar.

---
[⬅️ Volver a la Fábrica](../README.md) | [Siguiente: Laboratorio 🧪](../02_Entornos_Paquetes/02_guia_entornos.md)
