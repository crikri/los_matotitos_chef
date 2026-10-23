# from datos.modelos import Usuarios
from datos.conexion import conectar_db
from datos.modelos.usuario import Usuario


def guardar_usuario(usuario):
    db = conectar_db()
    db.connect()
    usuario.save()
    db.close()
