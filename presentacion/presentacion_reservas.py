from negocio.negocio_reservas import cargar_reservas, crear_reserva
from prettytable import PrettyTable
from datos.repositorio.repositorio_reservas import reserva_por_id, guardar_reserva

def mostrar_reservas():
    tabla = PrettyTable()
    tabla = cargar_reservas(tabla)
    print("\n--- LISTA DE RESERVAS ---")
    print(tabla)

def datos_reserva_crear():
    print("\n--- REGISTRAR NUEVA RESERVA ---")
    cant = input("Cantidad de personas: ")
    cliente = input("ID del Cliente: ")
    estado = input("ID del Estado de reserva: ")
    fecha = input("Fecha (YYYY-MM-DD): ")
    inicio = input("Hora de inicio (HH:MM): ")
    termino = input("Hora de término (HH:MM): ")
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