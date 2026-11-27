from prettytable import PrettyTable
from datos.repositorio.repositorio_clientes import listado_clientes, guardar_cliente, cliente_por_id
from datos.modelos.cliente import Cliente


def cargar_clientes(tabla: PrettyTable):
    clientes_db = listado_clientes()
    tabla.field_names = ['ID', 'RUT', 'Nombre', 'Apellido', 'Teléfono', 'Email']

    if clientes_db:
        for c in clientes_db:
            tabla.add_row([c.id_cliente, c.rut, c.nombre,
                           c.apellido, c.telefono, c.email])
    return tabla


def crear_cliente(rut, nombre, apellido, telefono, email):
    """Guarda un cliente nuevo y lo retorna (o None si falló)."""
    nuevo_cliente = Cliente()
    nuevo_cliente.rut = rut
    nuevo_cliente.nombre = nombre
    nuevo_cliente.apellido = apellido
    nuevo_cliente.telefono = telefono
    nuevo_cliente.email = email
    nuevo_cliente.habilitado = True

    resultado = guardar_cliente(nuevo_cliente)
    if resultado == 1:
        print(f'Se ha guardado el cliente con ID: {nuevo_cliente.id_cliente}')
        return nuevo_cliente
    return None


def nombre_cliente(id_cliente):
    """Texto 'RUT - Nombre Apellido' para mostrar en listados (ej. reservas)."""
    cliente = cliente_por_id(id_cliente)
    if cliente:
        return f'{cliente.rut} - {cliente.nombre} {cliente.apellido}'
    return f'Cliente {id_cliente} (no encontrado)'
