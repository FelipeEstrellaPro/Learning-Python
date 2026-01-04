# Testing: El Estándar de Calidad

## 1. Unittest vs Pytest
- **Unittest**: Viene en la librería estándar (no requiere instalación). Es verboso, basado en clases (inspirado en JUnit de Java).
- **Pytest**: De facto estándar moderno. Sintaxis limpia (usa `assert`), features poderosos (fixtures, parametrize). Requiere `pip install pytest`.

## 2. Conceptos Clave

### Aserciones (`assert`)
En unittest: `self.assertEqual(a, b)`
En pytest: `assert a == b` (pytest introspecciona el fallo y te dice exactamente por qué falló).

### Fixtures (`@pytest.fixture`)
Reemplazan al `setUp` y `tearDown`. Permiten inyectar dependencias (datos de prueba, conexiones a BD) a los tests que las necesiten. Son modulares y reutilizables.

### Parametrización
Ejecutar el mismo test con múltiples entradas.
`@pytest.mark.parametrize`

### Mocking (`unittest.mock`)
Simular partes del sistema (APIs externas, DBs) para aislar lo que estás probando.

## 3. Estructura de un Test
1. **Arrange**: Preparar el entorno.
2. **Act**: Ejecutar la función.
3. **Assert**: Verificar el resultado.
