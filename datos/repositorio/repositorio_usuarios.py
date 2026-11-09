from peewee import JOIN
from datos.modelos.usuario import Usuario
from datos.modelos.pais import Pais

def listado_usuarios_habilitados():
    try:
        usuarios = (Usuario
                    .select(Usuario, Pais)
                    .join(Pais, JOIN.LEFT_OUTER, on=(Usuario.pais == Pais.id_pais))
                    .where(Usuario.habilitado == True))
        return list(usuarios)
    except Exception as e:
        print(f"Error al obtener la lista de usuarios: {e}")
        return []

def guardar_usuario(datos_usuario: dict) -> bool:
    try:
        
        Usuario.create(**datos_usuario)
        return True
    except Exception as e:
        print(f"Error en la base de datos al crear usuario: {e}")
        return False