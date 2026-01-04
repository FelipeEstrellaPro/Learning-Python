import asyncio
import time

# Simula una llamada a una API o base de datos que tarda 1 segundo
async def consultar_datos(id):
    print(f"--> Iniciando consulta ID {id}")
    await asyncio.sleep(1) # Importante: asyncio.sleep, NO time.sleep
    print(f"<-- Terminada consulta ID {id}")
    return f"Dato {id}"

# Versión Síncrona (Bloqueante) para comparar
def consultar_datos_sync(id):
    print(f"--> Iniciando consulta (sync) ID {id}")
    time.sleep(1)
    print(f"<-- Terminada consulta (sync) ID {id}")
    return f"Dato {id}"

async def main():
    print("--- 1. Ejecución Secuencial (Lento) ---")
    start = time.perf_counter()
    # Espera uno por uno
    await consultar_datos(1)
    await consultar_datos(2)
    await consultar_datos(3)
    end = time.perf_counter()
    print(f"Tiempo Secuencial: {end - start:.2f} s (Esperado: ~3s)")

    print("\n--- 2. Ejecución Concurrente (Asyncio Gather) ---")
    start = time.perf_counter()
    # Lanza todos a la vez y espera que todos terminen
    resultados = await asyncio.gather(
        consultar_datos(1),
        consultar_datos(2),
        consultar_datos(3)
    )
    end = time.perf_counter()
    print(f"Resultados: {resultados}")
    print(f"Tiempo Concurrente: {end - start:.2f} s (Esperado: ~1s)")

if __name__ == "__main__":
    # Punto de entrada para asyncio
    asyncio.run(main())
