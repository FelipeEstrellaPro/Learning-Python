from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# 1. Definición del Modelo (Schema)
class Item(BaseModel):
    nombre: str
    precio: float
    en_oferta: bool = False

# 2. Inicializar App
app = FastAPI()

# 3. Endpoints
@app.get("/")
def read_root():
    return {"mensaje": "Hola Mundo desde FastAPI"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "info": "Aquí irían datos de DB"}

@app.post("/items/")
async def create_item(item: Item):
    # FastAPI valida que el body cumpla con el modelo Item
    precio_final = item.precio
    if item.en_oferta:
        precio_final *= 0.8
    
    return {
        "nombre": item.nombre,
        "precio_final": precio_final,
        "status": "Creado exitosamente"
    }

if __name__ == "__main__":
    # Para correr en desarrollo:
    # python 01_ejemplo_web.py
    print("Corriendo servidor en http://127.0.0.1:8000")
    print("Documentación en http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000)
