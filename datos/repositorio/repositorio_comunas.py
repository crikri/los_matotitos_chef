from datos.conexion import conectar_db
from datos.modelos.comuna import Comuna

def listado_comunas():
    return Comuna.select()