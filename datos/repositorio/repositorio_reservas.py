from datos.modelos.reserva import Reserva
from datos.auxiliar import mensaje_error_orm

def listado_reservas():
    return Reserva.select().where(Reserva.habilitado == True)

def guardar_reserva(reserva: Reserva):
    try:
        return reserva.save()
    except Exception as error:
        print(f'{mensaje_error_orm} {error}')

def reserva_por_id(id_reserva):
    try:
        return Reserva.get_or_none(Reserva.id_reserva == int(id_reserva))
    except Exception as error:
        print(f"Error al buscar reserva: {error}")
        return None