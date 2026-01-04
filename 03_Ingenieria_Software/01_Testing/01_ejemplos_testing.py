import unittest
import pytest

# Función a probar
def calcular_descuento(precio, porcentaje):
    if precio < 0 or porcentaje < 0:
        raise ValueError("Valores negativos no permitidos")
    return precio * (1 - porcentaje)

# ---------------------------------------------------------
# 1. Estilo Unittest (Clásico)
# ---------------------------------------------------------
class TestCalculadora(unittest.TestCase):
    def test_descuento_valido(self):
        resultado = calcular_descuento(100, 0.1)
        self.assertEqual(resultado, 90.0)

    def test_valores_negativos(self):
        with self.assertRaises(ValueError):
            calcular_descuento(-100, 0.1)

# ---------------------------------------------------------
# 2. Estilo Pytest (Moderno)
# ---------------------------------------------------------

# Fixture: Setup reutilizable
@pytest.fixture
def datos_prueba():
    return {"precio": 200, "porcentaje": 0.5, "esperado": 100.0}

def test_descuento_simple(datos_prueba):
    res = calcular_descuento(datos_prueba["precio"], datos_prueba["porcentaje"])
    assert res == datos_prueba["esperado"]

# Parametrización: Correr test múltiples veces
@pytest.mark.parametrize("p, porc, esp", [
    (100, 0.1, 90.0),
    (50, 0.5, 25.0),
    (0, 0.2, 0.0),
])
def test_varios_casos(p, porc, esp):
    assert calcular_descuento(p, porc) == esp

if __name__ == "__main__":
    # Permite correr el archivo directamente con python
    # Pero para ver pytest en acción, ejecutar en terminal: pytest
    unittest.main()
