from datos.modelos.trabajador import Trabajador
from datos.auxiliar import mensaje_error_orm

def listado_trabajadores():
    # Devuelve solo los trabajadores que tienen el estado habilitado en True
    return Trabajador.select().where(Trabajador.habilitado == True)

def guardar_trabajador(trabajador: Trabajador):
    try:
        return trabajador.save()
    except Exception as error:
        print(f'{mensaje_error_orm} {error}')

def trabajador_por_id(id_trabajador):
    try:
        return Trabajador.get_or_none(Trabajador.id_trabajador == int(id_trabajador))
    except Exception as error:
        print(f"Error al buscar trabajador: {error}")
        return None