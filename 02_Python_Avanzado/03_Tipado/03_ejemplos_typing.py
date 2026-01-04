from typing import List, Dict, Optional, Union, Protocol, TypeVar

# 1. Variables y Funciones Básicas
# -------------------------------

edad: int = 25
nombre: str = "Felipe"

def saludar(nombre: str, veces: int) -> str:
    return (f"Hola {nombre} " * veces).strip()

# Generará error en mypy si descomentas:
# res = saludar("Ana", "tres") # Error: arg 2 debe ser int

# 2. Tipos Union y Optional (Python 3.10+ sintaxis simplificada)
# -------------------------------------------------------------

def dividir(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a / b

resultado = dividir(10, 2)
# Mypy te obligará a verificar si es None antes de operar con él si usas modo estricto

# 3. Protocol (Duck Typing formal)
# -----------------------------------------------

class Volador(Protocol):
    def volar(self) -> None:
        ...

class Pajaro:
    def volar(self) -> None:
        print("Pájaro volando")

class Avion:
    def volar(self) -> None:
        print("Avión despeganado")

class Perro:
    def ladrar(self) -> None:
        print("Guau")

def hacer_volar(objeto: Volador) -> None:
    objeto.volar()

# Funciona
hacer_volar(Pajaro())
hacer_volar(Avion())
# hacer_volar(Perro()) # Error estático: Perro no tiene metodo volar()

# 4. Generics
# -----------------------------------------------
T = TypeVar("T")

def obtener_primero(lista: list[T]) -> T | None:
    if not lista:
        return None
    return lista[0]

val_int = obtener_primero([1, 2, 3]) # Infiere retorno int
val_str = obtener_primero(["a", "b"]) # Infiere retorno str
