from datos.conexion import conectar_db
from datos.modelos.mesa import Mesa
from datos.auxiliar import mensaje_error_orm
db = conectar_db()


def listado_mesas():
    mesas_db = Mesa.select().where(Mesa.habilitado == True)
    return mesas_db


def guardar_mesa(mesa: Mesa):
    try:
        mesa_nueva = mesa.save()
        return mesa_nueva
    except Exception as error:
        print(f'{mensaje_error_orm} {error}')


def mesa_por_numero(numero):
    try:
        mesas_db = Mesa.select().where(Mesa.numero_mesa.contains(numero))
        if mesas_db:
            return mesas_db
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')


def mesa_por_id(id_mesa):
    try:
        return Mesa.get_or_none(Mesa.id_mesa == int(id_mesa))
    except Exception as error:
        print(f"Error al buscar mesa: {error}")
        return None
