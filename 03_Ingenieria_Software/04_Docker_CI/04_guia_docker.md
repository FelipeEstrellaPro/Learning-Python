# 🚢 Docker: El Contenedor de Envío

![Difficulty](https://img.shields.io/badge/Dificultad-Experto-red)

## 👶 Explicación para Niños (ELI5)

Imagina que preparaste una torta deliciosa en tu cocina. 🎂
La llevas a casa de tu amigo, pero allá no tienen horno, ni harina, ni batidora. ¡Desastre! 
Esto es el famoso: *"En mi máquina funciona"*.

Docker es como meter **TU COCINA ENTERA** (horno, ingredientes, chef) dentro de una caja mágica.
Envías la caja a tu amigo. Él solo abre la caja y la torta sale perfecta.
No importa si la casa de tu amigo es una cueva o un palacio. La caja siempre funciona igual por dentro.

## 🐳 Dockerfile (La Receta de la Caja)

Es un papel donde dices qué meter en la caja.

```dockerfile
# 1. Empieza con un sistema base (Una cocina vacía con Python)
FROM python:3.9

# 2. Mete tu código (La harina y los huevos)
COPY . /app

# 3. Instala lo que necesitas (La batidora)
RUN pip install fastapi

# 4. Di qué hacer al abrir la caja (Hornear!)
CMD ["python", "app.py"]
```

---
[⬅️ Anterior: LEGOs](../03_Clean_Code/03_guia_solid.md) | [Subir de Nivel: Mundo Real 🌍](../../04_Especializacion/README.md)
