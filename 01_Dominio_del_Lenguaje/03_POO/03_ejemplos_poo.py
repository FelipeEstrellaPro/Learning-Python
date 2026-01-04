import json

# 1. Mixins
class JsonSerializableMixin:
    """Añade capacidad de serialización a JSON a cualquier clase."""
    def to_json(self):
        # vars(self) devuelve el diccionario __dict__
        return json.dumps(vars(self))

# 2. Dunder Methods & Properties
class Producto(JsonSerializableMixin):
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio # Atributo "privado" por convención

    # __str__: Representación legible
    def __str__(self):
        return f"Producto: {self._nombre} (${self._precio})"

    # __repr__: Representación inambigua para devs
    def __repr__(self):
        return f"Producto(nombre='{self._nombre}', precio={self._precio})"

    # __add__: Sobrecarga operador +
    def __add__(self, otro):
        if isinstance(otro, Producto):
            return self._precio + otro._precio
        return NotImplemented

    # __call__: Instancia ejecutable como función
    def __call__(self, descuento=0):
        return self._precio * (1 - descuento)

    # @property: Getter
    @property
    def precio(self):
        return self._precio

    # @precio.setter: Setter con validación
    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

# --- Uso ---
p1 = Producto("Laptop", 1000)
p2 = Producto("Mouse", 50)

print("--- 1. ToString & Repr ---")
print(str(p1))  # Usa __str__
print(repr(p1)) # Usa __repr__

print("\n--- 2. Sobrecarga de Operadores (+) ---")
total = p1 + p2 # Usa __add__
print(f"Suma de precios: {total}")

print("\n--- 3. Callable Objetos ---")
# Usamos p1 como función gracias a __call__
precio_con_descuento = p1(0.10) # 10% descuento
print(f"Precio con 10% off: {precio_con_descuento}")

print("\n--- 4. Mixin (Herencia Múltiple) ---")
# p1 heredó to_json()
print(f"JSON: {p1.to_json()}")

print("\n--- 5. Properties (Validación) ---")
try:
    p1.precio = -200 # Dispara el setter y valida
except ValueError as e:
    print(f"Error capturado: {e}")
