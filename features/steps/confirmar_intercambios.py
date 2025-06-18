from behave import *

from src.Libro import Libro
from src.Estudiante import Estudiante
from src.Notificador import Notificador

use_step_matcher("re")

"""
    Solicitar confirmación al acercarse la fecha límite
"""

@step('que dos estudiantes han acordado un intercambio con fecha límite "(?P<fecha_limite>.+)"')
def step_impl(context, fecha_limite):
    libro1 = Libro("", Estudiante(""))
    libro2 = Libro("", Estudiante(""))

    notificador = Notificador()
    notificador.acordar_intercambio(libro1, libro2, fecha_limite)

    context.notificador = notificador
    context.intercambio = notificador.intercambios[0]
    assert len(context.notificador.intercambios) > 0

@step("faltan 24 horas para la fecha límite del intercambio")
def step_impl(context):
    fecha_actual = context.scenario._row["fecha_actual"]
    assert context.notificador.faltan_24_horas(fecha_actual, context.intercambio.fecha_limite)


@step("se solicita a ambos estudiantes que confirmen si realizarán el intercambio")
def step_impl(context):
    context.notificador.solicitar_confirmacion(context.intercambio)
    assert context.intercambio.estado == "En espera de confirmación"

"""
    Intercambio confirmado por ambos estudiantes
"""

@step('que ambos estudiantes han confirmado el intercambio antes de la fecha límite')
def step_impl(context):

    intercambio = context.intercambio

    fecha_confirmacion_1 = context.scenario._row["fecha_confirmacion_1"]
    fecha_confirmacion_2 = context.scenario._row["fecha_confirmacion_2"]

    intercambio.confirmar(intercambio.libro1.estudiante, fecha_confirmacion_1)
    intercambio.confirmar(intercambio.libro2.estudiante, fecha_confirmacion_2)

    assert all(intercambio.confirmaciones.values())


@step("se alcanzó la fecha límite")
def step_impl(context):
   assert context.notificador.es_fecha_limite(context.scenario._row["fecha_actual"], context.scenario._row["fecha_limite"])


@step("el intercambio se registra como exitoso")
def step_impl(context):
    pass