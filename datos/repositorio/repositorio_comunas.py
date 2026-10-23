from datos.conexion import conectar_db
from datos.modelos.comuna import Comuna
from datos.auxiliar import mensaje_error_orm
db = conectar_db()


def listado_comunas():
    comunas = Comuna.select().where(Comuna.habilitado == True)
    return comunas
    
def listado_comunas_deshabilitadas():
    comunas = Comuna.select().where(Comuna.habilitado == False)
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


def comuna_por_id(id_comuna):
    try:
        return Comuna.get_or_none(Comuna.id_comuna == int(id_comuna))
    except Exception as error:
        print(f"Error al buscar comuna: {error}")
        return None
