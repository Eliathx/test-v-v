from src.Intercambio import Intercambio
from datetime import datetime, timedelta

class Notificador:
    def __init__(self):
        self.intercambios = []

    def acordar_intercambio(self, libro1, libro2, fecha_limite):
        nuevo_intercambio = Intercambio(libro1, libro2, fecha_limite)
        self.intercambios.append(nuevo_intercambio)

    def faltan_24_horas(self, fecha_actual, fecha_limite):

        fecha_actual_dt = datetime.strptime(fecha_actual, "%Y-%m-%d %H:%M")
        fecha_limite_dt = datetime.strptime(fecha_limite, "%Y-%m-%d %H:%M")

        diferencia = fecha_limite_dt - fecha_actual_dt
        return timedelta(0) < diferencia <= timedelta(hours=24)

    def excede_fecha_limite(self, fecha_de_confirmacion, fecha_limite):
        fecha_de_confirmacion_dt = datetime.strptime(fecha_de_confirmacion, "%Y-%m-%d %H:%M")
        fecha_limite_dt = datetime.strptime(fecha_limite, "%Y-%m-%d %H:%M")

        return fecha_de_confirmacion_dt > fecha_limite_dt

    def es_fecha_limite(self, fecha_actual, fecha_limite):
        fecha_actual_dt = datetime.strptime(fecha_actual, "%Y-%m-%d %H:%M")
        fecha_limite_dt = datetime.strptime(fecha_limite, "%Y-%m-%d %H:%M")

        return fecha_actual_dt == fecha_limite_dt

    def solicitar_confirmacion(self, intercambio):
        intercambio.solicitar_confirmacion()



