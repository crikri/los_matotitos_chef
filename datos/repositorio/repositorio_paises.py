from datos.conexion import conectar_db
from datos.modelos.pais import Pais

database = conectar_db()

def listado_paises():
    listado_paises = Pais.select()
    return listado_paises

def obtener_pais_nombre(nombre):
    try:
        paises = Pais.select().where(Pais.nombre.contains(nombre))
        if paises:
            return paises
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def obtener_pais_id(id_pais):
    try:
        return Pais.get_or_none(Pais.id_pais == id_pais)
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')
        return None

def guardar_pais():
    print('GG')

def actualizar_pais():
    print('GG')

def eliminar_pais():
    print('GG')