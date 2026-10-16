from datos.conexion import conectar_db
from datos.modelos.comuna import Comuna

db = conectar_db()


def listado_comunas():
    comunas = Comuna.select()
    return comunas


def guardar_comuna(comuna: Comuna):
    try:
        comuna_nueva = comuna.save()
        return comuna_nueva
    except Exception as error:
        print(f'{mensaje_error_orm} {error}')


def comuna_por_nombre(nombre):
    try:
        comunas = Comuna.select().where(Comuna.comuna.contains(nombre))
        if comunas:
            return comunas
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')


def comuna_por_id(id):
    try:
        comuna = Comuna[id]
        if comuna:
            return comuna
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')
