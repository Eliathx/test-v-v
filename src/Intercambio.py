from datetime import datetime

class Intercambio:
    def __init__(self, libro1, libro2, fecha_limite):
        self.libro1 = libro1
        self.libro2 = libro2
        self.fecha_limite = fecha_limite
        self.estado = "Nuevo"
        self.confirmaciones = {
            libro1.estudiante: False,
            libro2.estudiante: False
        }

    def solicitar_confirmacion(self):
        self.estado = "En espera de confirmación"

    def confirmar(self, estudiante, fecha_de_confirmacion):
        fecha_conf_dt = datetime.strptime(fecha_de_confirmacion, "%Y-%m-%d %H:%M")
        fecha_limite_dt = datetime.strptime(self.fecha_limite, "%Y-%m-%d %H:%M")

        if fecha_conf_dt <= fecha_limite_dt:
            self.confirmaciones[estudiante] = True
        else:
            self.confirmaciones[estudiante] = False

    def verificar_confirmaciones(self):
        if all(self.confirmaciones.values()):
            self.estado = "Exitoso"
        else:
            self.estado = "Fallido"
