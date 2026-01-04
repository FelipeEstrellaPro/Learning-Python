# 🌐 Web: La Pizzería API (FastAPI)

![Difficulty](https://img.shields.io/badge/Dificultad-Divertida-purple)

## 👶 Explicación para Niños (ELI5)

Una **API** es como un camarero. 🤵
1.  Tú (Cliente) le pides: *"Quiero una pizza de pepperoni"* (Request).
2.  El camarero va a la cocina, le dice al cocinero, y vuelve con la pizza.
3.  Te la entrega: *"Aquí tiene"* (Response).

Si no hubiera camarero (API), tendrías que entrar tú a la cocina a cocinar. (Peligroso y sucio).

---

## 🍕 Tu Proyecto: Pizza-Net

Vamos a crear un camarero digital usando **FastAPI**.
Es el camarero más rápido del oeste.

### El Menú (Modelos)
```python
class Pizza(BaseModel):
    sabor: str
    precio: float
    extra_queso: bool = False
```

### Tomar la Orden (Endpoint)
```python
@app.post("/pedir/")
async def cocinar_pizza(pizza: Pizza):
    if pizza.extra_queso:
        return f"¡{pizza.sabor} con MUCHO queso lista!"
    return f"¡{pizza.sabor} lista!"
```

**¡Eso es todo!** Acabas de crear un backend.

---
[⬅️ Volver al Mapa](../README.md) | [Siguiente: Analista Pokémon 📊](../02_Data_Science/02_guia_data.md)
