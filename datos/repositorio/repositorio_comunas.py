from datos.conexion import conectar_db
from datos.modelos.comuna import Comuna

def listado_comunas():
    comunas = Comuna.select()
    return comunas

def guardar_comuna(comuna: Comuna):
    comuna_nueva = comuna.save()
    return comuna_nueva