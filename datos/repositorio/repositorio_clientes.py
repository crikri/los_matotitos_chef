# from datos.modelos import Clientes
from datos.conexion import conectar_db
from datos.modelos.cliente import Cliente


def guardar_cliente(cliente):
    db = conectar_db()
    db.connect()
    cliente.save()
    db.close()
