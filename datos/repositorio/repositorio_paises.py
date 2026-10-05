from datos.conexion import conectar_db
from datos.modelos.pais import Pais

def listado_paises():
    return Pais.select()

def guardar_pais(pais):
    db = conectar_db()
    db.connect()
    pais.save()
    db.close()