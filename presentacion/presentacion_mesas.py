from negocio.negocio_mesas import obtener_datos_mesa, cargar_mesas, crear_mesa, buscar_mesas
from prettytable import PrettyTable
from datos.repositorio.repositorio_mesas import mesa_por_id, guardar_mesa


def mostrar_mesas():
    tabla_mesas = PrettyTable()
    tabla_mesas = cargar_mesas(tabla_mesas)
    print(tabla_mesas)


def datos_mesa_crear():
    capacidad = input("Ingrese capacidad de la mesa: ")
    estado = input("Ingrese estado (ej. D=Disponible, O=Ocupada): ")
    restaurante = input("Ingrese ID del restaurante al que pertenece: ")
    numero_mesa = input("Ingrese número o código de mesa: ")
    crear_mesa(capacidad, estado, restaurante, numero_mesa)


def buscar_mesa_numero(numero):
    tabla_mesas = PrettyTable()
    tabla_mesas = buscar_mesas(tabla_mesas, numero)
    print(tabla_mesas)


def actualizar_mesa():
    mostrar_mesas()

    numero = input("Ingrese número de mesa para buscar: ")
    buscar_mesa_numero(numero)
    id_ingresado = input("Ingrese Id de la mesa para modificar: ")
    mesa = mesa_por_id(id_ingresado)

    if not mesa:
        print("Mesa no encontrada.")
        return

    capacidad_nueva = input(
        "Ingrese nueva capacidad (o ENTER para conservar): ")
    estado_nuevo = input("Ingrese nuevo estado (o ENTER para conservar): ")
    restaurante_nuevo = input(
        "Ingrese nuevo ID de restaurante (o ENTER para conservar): ")
    numero_nuevo = input(
        "Ingrese nuevo número de mesa (o ENTER para conservar): ")

    if capacidad_nueva != '':
        mesa.capacidad = capacidad_nueva
    if estado_nuevo != '':
        mesa.estado = estado_nuevo
    if restaurante_nuevo != '':
        mesa.restaurante = restaurante_nuevo
    if numero_nuevo != '':
        mesa.numero_mesa = numero_nuevo

    respuesta = guardar_mesa(mesa)
    if respuesta == 1:
        print("Mesa actualizada correctamente")


def eliminar_mesa():
    mostrar_mesas()
    numero = input('Ingrese Número de Restaurante para buscar: ')
    buscar_mesa_numero(numero)

    entrada = input('Ingrese Id de Mesa para eliminar: ')
    if not entrada.isdigit():
        print('El ID debe ser un número entero válido.')
        return

    mesa = mesa_por_id(entrada)
    if not mesa:
        print(f'No se encontró la mesa con ID {entrada}.')
        return

    mesa.habilitado = False
    respuesta = guardar_mesa(mesa)

    if respuesta == 1:
        print(f'Mesa {mesa.numero_mesa} eliminada con éxito.')
    else:
        print('No se pudo actualizar el estado de la mesa.')


def datos_mesa(numero):
    tabla_mesas = PrettyTable()
    tabla_mesas = buscar_mesas(tabla_mesas, numero)
    print(tabla_mesas)

    print("\n--- CONSULTAR DATOS DE MESA ---")
    entrada = input("Ingrese el ID de la mesa: ")

    if not entrada.isdigit():
        print("El ID debe ser un número entero válido.")
        return

    mesa = obtener_datos_mesa(entrada)

    if not mesa:
        print(f"No se encontró ninguna mesa con el ID {entrada}.")
        return

    estado_hab = "Habilitada" if getattr(
        mesa, 'habilitado', True) else "Deshabilitada"

    print("\n================================")
    print(f" ID         : {mesa._pk}")
    print(f" N° Mesa    : {mesa.numero_mesa}")
    print(f" Capacidad  : {mesa.capacidad}")
    print(f" Estado     : {mesa.estado}")
    print(f" ID Rest.   : {mesa.restaurante}")
    print(f" Habilitada : {estado_hab}")
    print("================================\n")
