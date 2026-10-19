from datos.repositorio.repositorio_reservas import listado_reservas, guardar_reserva, reserva_por_id
from prettytable import PrettyTable
from datos.modelos.reserva import Reserva

def cargar_reservas(tabla: PrettyTable):
    reservas_db = listado_reservas()
    tabla.field_names = ['ID', 'Personas', 'ID Cliente', 'ID Mesa', 'Fecha', 'Inicio', 'Término']

    if reservas_db:
        for r in reservas_db:
            tabla.add_row([
                r.id_reserva, r.cantidad_personas, r.cliente, 
                r.mesa, r.fecha, r.hora_inicio, r.hora_termino
            ])
    return tabla

def crear_reserva(cant_personas, cliente, estado, fecha, hora_inicio, hora_termino, mesa):
    nueva_reserva = Reserva()
    nueva_reserva.cantidad_personas = cant_personas
    nueva_reserva.cliente = cliente
    nueva_reserva.estado = estado
    nueva_reserva.fecha = fecha
    nueva_reserva.hora_inicio = hora_inicio
    nueva_reserva.hora_termino = hora_termino
    nueva_reserva.mesa = mesa
    nueva_reserva.habilitado = True
    
    resultado = guardar_reserva(nueva_reserva)
    if resultado == 1:
        print(f'Se ha guardado la reserva con ID: {nueva_reserva.id_reserva}')