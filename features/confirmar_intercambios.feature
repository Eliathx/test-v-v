# Created by Eliathx at 18/6/2025
#  language: es

  # Capability:  Seguimiento de intercambios
Característica: Confirmación de intercambio de libros
  Como estudiante que ha acordado un intercambio de libros
  Quiero recibir recordatorios para confirmar el intercambio antes del plazo
  Para que no se me olvide concretarlo

  Esquema del escenario: Solicitar confirmación al acercarse la fecha límite
    Dado que dos estudiantes han acordado un intercambio con fecha límite "<fecha_limite>"
    Cuando faltan 24 horas para la fecha límite del intercambio
    Entonces se solicita a ambos estudiantes que confirmen si realizarán el intercambio

    Ejemplos:
      | fecha_limite        | fecha_actual         |
      | 2025-11-06 18:00    | 2025-11-05 18:00     |
      | 2025-11-06 11:00    | 2025-11-05 11:00     |
      | 2025-11-06 08:00    | 2025-11-05 08:00     |

  Esquema del escenario: Intercambio confirmado por ambos estudiantes
    Dado que dos estudiantes han acordado un intercambio con fecha límite "<fecha_limite>"
    Y que ambos estudiantes han confirmado el intercambio antes de la fecha límite
    Cuando se alcanzó la fecha límite
    Entonces el intercambio se registra como exitoso

    Ejemplos:
      | fecha_limite        | fecha_confirmacion_1 | fecha_confirmacion_2 | fecha_actual |
      | 2025-11-06 18:00    | 2025-11-05 12:00      | 2025-11-05 16:00      |2025-11-06 18:00  |
      | 2025-11-07 10:00    | 2025-11-06 08:30      | 2025-11-06 09:00      |2025-11-07 10:00 |

"""
  Escenario: Intercambio no confirmado por ambos estudiantes
    Dado que solo uno o ninguno de los estudiantes ha confirmado el intercambio antes de la fecha límite
    Cuando se alcanzó la fecha límite
    Entonces el intercambio se registra como fallido

"""
