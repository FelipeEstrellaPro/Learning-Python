# Clean Code y SOLID en Python

## 1. PEP 8 y Tooling
No pierdas tiempo discutiendo formato. Usa herramientas automáticas.
- **Ruff**: Linter/Formatter ultrarrápido (reemplaza a Flake8/Black/Isort).
- **Black**: El "uncompromising code formatter".

## 2. Principios SOLID

### S - Single Responsibility (Responsabilidad Única)
Una clase debe tener **una sola razón para cambiar**.
*Mal*: Una clase `Usuario` que guarda en BD y envía emails.
*Bien*: `Usuario` (datos), `UsuarioRepository` (BD), `EmailService` (correos).

### O - Open/Closed (Abierto/Cerrado)
Abierto a extensión, cerrado a modificación. Usa polimorfismo o inyección de dependencias para agregar comportamientos sin tocar código viejo.

### L - Liskov Substitution (Sustitución de Liskov)
Las subclases deben poder reemplazar a sus padres sin romper el programa.
Si tu subclase lanza error en un método que el padre no, viola Liskov.

### I - Interface Segregation (Segregación de Interfaces)
Mejor muchas interfaces pequeñas y específicas que una gigante ("God Interface"). En Python se usa `Protocol`.

### D - Dependency Inversion (Inversión de Dependencias)
Depende de abstracciones, no de concreciones.
En lugar de `def guardar(db: MySQL)`, usa `def guardar(db: DatabaseInterface)`.
