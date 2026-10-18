from datos.modelos.restaurante import Restaurante
from datos.conexion import conectar_db

db = conectar_db()


def insertar_restaurante(nombre, direccion, email, telefono, website=None):
    try:
        nuevo_restaurante = Restaurante.create(
            nombre=nombre,
            direccion=direccion,
            email=email,
            telefono=telefono,
            website=website,
            habilitado=True
        )
        return nuevo_restaurante
    except Exception as error:
        print(f"Error al registrar restaurante en la base de datos: {error}")
        return None


def listado_restaurantes():
    try:
        # Si tiene campo habilitado/activo:
        return Restaurante.select().where(Restaurante.habilitado == True)
        # Si no tiene borrado lógico aún: return Restaurante.select()
    except Exception as error:
        print(f"Error al listar restaurantes: {error}")
        return []


def restaurante_por_id(id_rest):
    try:
        return Restaurante.get_or_none(Restaurante.id_restaurantes == int(id_rest))
    except Exception as error:
        print(f"Error al buscar restaurante por ID: {error}")
        return None


def guardar_restaurante(restaurante: Restaurante):
    try:
        filas_afectadas = restaurante.save()
        return filas_afectadas
    except Exception as error:
        print(f"Error al actualizar restaurante en la BD: {error}")
        return None
