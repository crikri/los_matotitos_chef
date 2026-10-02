from datos.models import Clientes
from datos.conexion import conectar_db

def guardar_autor(cliente):
    db = conectar_db()
    db.connect()
    cliente.save()
    db.close()
