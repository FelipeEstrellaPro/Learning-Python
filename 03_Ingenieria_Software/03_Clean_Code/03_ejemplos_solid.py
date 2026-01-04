from abc import ABC, abstractmethod

# ---------------------------------------------------------
# VIOLACIÓN DE SOLID (Anti-patrón)
# ---------------------------------------------------------
class ReporteMonolitico:
    """Viola SRP (hace todo) y OCP (difícil extender formatos)."""
    def __init__(self, datos):
        self.datos = datos

    def generar(self):
        print(f"Generando reporte: {self.datos}")

    def guardar_archivo(self):
        print("Guardando en archivo.txt...")

    def enviar_email(self):
        print("Enviando email...")

# ---------------------------------------------------------
# APLICANDO SOLID
# ---------------------------------------------------------

# 1. Single Responsibility: Clase de datos
class Reporte:
    def __init__(self, datos):
        self.datos = datos

# 2. Open/Closed & Dependency Inversion: Interfaz para persistencia
class Persistencia(ABC):
    @abstractmethod
    def guardar(self, reporte: Reporte):
        pass

class GuardarArchivo(Persistencia):
    def guardar(self, reporte: Reporte):
        print(f"SOLID: Guardando {reporte.datos} en disco.")

class GuardarNube(Persistencia):
    def guardar(self, reporte: Reporte):
        print(f"SOLID: Subiendo {reporte.datos} a AWS.")

# 3. Interfaz Segregada para Notificaciones
class Notificable(ABC):
    @abstractmethod
    def enviar(self, msg):
        pass

class Email(Notificable):
    def enviar(self, msg):
        print(f"Email enviado: {msg}")

# Orquestador (Inyección de Dependencias)
class GestorReportes:
    def __init__(self, persistencia: Persistencia, notificador: Notificable):
        self.persistencia = persistencia
        self.notificador = notificador

    def procesar(self, reporte: Reporte):
        self.persistencia.guardar(reporte)
        self.notificador.enviar("Reporte procesado")

# Uso
rep = Reporte("Ventas 2024")
# Podemos cambiar la estrategia de guardado sin tocar GestorReportes (OCP, DIP)
gestor = GestorReportes(GuardarNube(), Email())
gestor.procesar(rep)
