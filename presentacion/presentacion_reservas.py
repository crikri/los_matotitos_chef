from datetime import datetime
from presentacion.presentacion_clientes import seleccionar_cliente
from negocio.negocio_reservas import cargar_reservas, crear_reserva
from prettytable import PrettyTable
from datos.repositorio.repositorio_reservas import reserva_por_id, guardar_reserva
from presentacion.presentacion_mesas import mostrar_mesas


def mostrar_reservas():
    tabla = PrettyTable()
    tabla = cargar_reservas(tabla)
    print("\n--- LISTA DE RESERVAS ---")
    print(tabla)


def datos_reserva_crear():
    print("\n--- REGISTRAR NUEVA RESERVA ---")
    cant = input("Cantidad de personas: ")
    cliente = seleccionar_cliente()
    if cliente is None:
        print("No se registró la reserva: falta el cliente.")
        return
    estado = input("ID del Estado de reserva: ")
    fecha = input("Fecha (YYYY-MM-DD): ")
    inicio = input("Hora de inicio (HH:MM): ")
    termino = input("Hora de término (HH:MM): ")
    mostrar_mesas()
    mesa = input("ID de la Mesa: ")

    crear_reserva(cant, cliente, estado, fecha, inicio, termino, mesa)


def eliminar_reserva():
    print("\n--- ELIMINAR RESERVA ---")
    entrada = input('Ingrese ID de la Reserva para eliminar (Lógico): ')

    if not entrada.isdigit():
        print('El ID debe ser un número.')
        return

    reserva = reserva_por_id(entrada)
    if not reserva:
        print(f'No se encontró la reserva con ID {entrada}.')
        return

    reserva.habilitado = False
    if guardar_reserva(reserva) == 1:
        print('Reserva eliminada con éxito.')


def modificar_reserva():

    mostrar_reservas()
    numero = input("Ingrese el id de la reserva: ")
    reserva = reserva_por_id(numero)

    cantidad_nueva = input(
        "Ingrese nueva cantidad de personas (o ENTER para conservar): ")
    cambiar_cliente = input(
        "¿Cambiar el cliente por otro RUT? (s o ENTER para conservar): ")
    cliente_nuevo = ''
    if cambiar_cliente.lower() == 's':
        id_nuevo = seleccionar_cliente()
        if id_nuevo is not None:
            cliente_nuevo = str(id_nuevo)
    estado_nuevo = input("Ingrese nuevo estado (o ENTER para conservar): ")
    fecha_nueva = input(
        "Ingrese nueva fecha YYYY-MM-DD (o ENTER para conservar): ")
    hora_inicio_nueva = input(
        "Ingrese nueva hora de inicio HH:MM (o ENTER para conservar): ")
    hora_termino_nueva = input(
        "Ingrese nueva hora de término HH:MM (o ENTER para conservar): ")
    mesa_nueva = input("Ingrese nuevo ID de mesa (o ENTER para conservar): ")
    habilitado_nuevo = input(
        "¿Reserva habilitada? (s/n o ENTER para conservar): ")

    if cantidad_nueva != '':
        reserva.cantidad_personas = int(cantidad_nueva)
    if cliente_nuevo != '':
        reserva.cliente = int(cliente_nuevo)
    if estado_nuevo != '':
        reserva.estado = int(estado_nuevo)
    if fecha_nueva != '':
        reserva.fecha = datetime.strptime(fecha_nueva, "%Y-%m-%d").date()
    if hora_inicio_nueva != '':
        reserva.hora_inicio = datetime.strptime(
            hora_inicio_nueva, "%H:%M").time()
    if hora_termino_nueva != '':
        reserva.hora_termino = datetime.strptime(
            hora_termino_nueva, "%H:%M").time()
    if mesa_nueva != '':
        reserva.mesa = int(mesa_nueva)
    if habilitado_nuevo != '':
        reserva.habilitado = habilitado_nuevo.lower() == 's'

    respuesta = guardar_reserva(reserva)

    if respuesta == 1:
        print("Comuna actualizada correctamente")
