from datos.modelos.cliente import Cliente
from auxiliar.auxiliar import mensaje_error_orm


def listado_clientes():
    return Cliente.select().where(Cliente.habilitado == True)


def guardar_cliente(cliente: Cliente):
    try:
        return cliente.save()
    except Exception as error:
        print(f'{mensaje_error_orm} {error}')


def cliente_por_id(id_cliente):
    try:
        return Cliente.get_or_none(Cliente.id_cliente == int(id_cliente))
    except Exception as error:
        print(f"Error al buscar cliente: {error}")
        return None


def cliente_por_rut(rut):
    """Busca por RUT ya normalizado (ver normalizar_rut). Incluye clientes deshabilitados."""
    try:
        return Cliente.get_or_none(Cliente.rut == rut)
    except Exception as error:
        print(f"Error al buscar cliente: {error}")
        return None
