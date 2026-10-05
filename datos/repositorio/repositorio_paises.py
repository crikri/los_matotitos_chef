from datos.conexion import conectar_db
from datos.modelos.pais import Pais


def listado_paises():
    return Pais.select()


def guardar_cliente(cliente):
    db = conectar_db()
    db.connect()
    cliente.save()
    db.close()
