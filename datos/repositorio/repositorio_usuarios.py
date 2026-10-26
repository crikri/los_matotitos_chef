from datos.modelos.usuario import Usuario

def listado_usuarios_habilitados():
    try:
        # Retorna todos los usuarios que tengan el estado habilitado en True
        usuarios = Usuario.select().where(Usuario.habilitado == True)
        return list(usuarios)
    except Exception as e:
        print(f"Error al obtener la lista de usuarios: {e}")
        return []

def guardar_usuario(datos_usuario: dict) -> bool:
    try:
        # Se insertan los datos desempaquetando el diccionario
        Usuario.create(**datos_usuario)
        return True
    except Exception as e:
        print(f"Error en la base de datos al crear usuario: {e}")
        return False