class DineroInsuficienteError(Exception):
    """Excepción personalizada para cuando eres pobre 💸"""
    pass

class Billetera:
    def __init__(self, saldo):
        self.saldo = saldo

    def comprar(self, precio):
        print(f"Intentando comprar algo de ${precio}...")
        if precio > self.saldo:
            # Lanzamos nuestro propio error
            raise DineroInsuficienteError(f"Te faltan ${precio - self.saldo}")
        
        self.saldo -= precio
        print("¡Compra exitosa! 🎉")

# --- El show del Trapecista ---

mi_billetera = Billetera(100)

try:
    # Salto 1: Fácil
    mi_billetera.comprar(50)
    
    # Salto 2: Mortal (Cuesta 200 y solo tengo 50)
    mi_billetera.comprar(200)

except DineroInsuficienteError as e:
    # Atrapamos nuestro error custom
    print(f"🥅 RED DE SEGURIDAD ACTIVADA: {e}")

except Exception as e:
    # Atrapamos cualquier otra cosa
    print(f"💥 Error desconocido: {e}")

finally:
    print(f"--- Fin de la transacción. Saldo final: ${mi_billetera.saldo} ---")
