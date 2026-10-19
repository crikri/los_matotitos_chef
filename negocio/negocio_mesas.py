from datos.repositorio.repositorio_mesas import listado_mesas, guardar_mesa, mesa_por_numero, mesa_por_id
from prettytable import PrettyTable
from datos.modelos.mesa import Mesa


def cargar_mesas(tabla: PrettyTable):
    mesas_db = listado_mesas()
    tabla.field_names = ['Id', 'Capacidad', 'Estado', 'ID Rest.', 'N° Mesa']

    if mesas_db:
        for mesa in mesas_db:
            tabla.add_row(
                [mesa.id_mesa, mesa.capacidad, mesa.estado, mesa.restaurante, mesa.numero_mesa])

    return tabla


def buscar_mesas(tabla: PrettyTable, numero):
    mesas_db = mesa_por_numero(numero)
    tabla.field_names = ['Id', 'Capacidad', 'Estado',
                         'ID Rest.', 'N° Mesa', 'Habilitado']

    if mesas_db:
        for mesa in mesas_db:
            tabla.add_row(
                [mesa.id_mesa, mesa.capacidad, mesa.estado, mesa.restaurante, mesa.numero_mesa, mesa.habilitado])

    return tabla


def crear_mesa(capacidad, estado, restaurante, numero_mesa):
    nueva_mesa = Mesa()
    nueva_mesa.capacidad = capacidad
    nueva_mesa.estado = estado
    nueva_mesa.restaurante = restaurante
    nueva_mesa.numero_mesa = numero_mesa
    nueva_mesa.habilitado = True

    mesa = guardar_mesa(nueva_mesa)
    if mesa == 1:
        print(
            f'Se ha guardado la mesa {nueva_mesa.numero_mesa} con ID: {nueva_mesa.id_mesa}')


def obtener_datos_mesa(id_mesa):
    mesa = mesa_por_id(id_mesa)
    return mesa
