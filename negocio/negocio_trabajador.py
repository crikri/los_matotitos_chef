from datos.repositorio.repositorio_trabajador import listado_trabajadores, guardar_trabajador, trabajador_por_id
from prettytable import PrettyTable
from datos.modelos.trabajador import Trabajador

def cargar_trabajadores(tabla: PrettyTable):
    trabajadores_db = listado_trabajadores()
    # Definimos las cabeceras de la tabla según los campos de tu modelo
    tabla.field_names = ['ID', 'Nombre', 'Apellido', 'Nacimiento', 'ID Nac.', 'ID Dir.', 'Teléfono']

    if trabajadores_db:
        for t in trabajadores_db:
            # Agregamos cada fila de la base de datos a la tabla visual
            tabla.add_row([
                t.id_trabajador, t.nombre, t.apellido, 
                t.fecha_nacimiento, t.nacionalidad, t.direccion, t.telefono
            ])
    return tabla

def crear_trabajador(nombre, apellido, fecha_nacimiento, nacionalidad, direccion, telefono):
    # Instanciamos un nuevo trabajador
    nuevo_trabajador = Trabajador()
    nuevo_trabajador.nombre = nombre
    nuevo_trabajador.apellido = apellido
    nuevo_trabajador.fecha_nacimiento = fecha_nacimiento
    nuevo_trabajador.nacionalidad = nacionalidad
    nuevo_trabajador.direccion = direccion
    nuevo_trabajador.telefono = telefono
    nuevo_trabajador.habilitado = True # Aseguramos que nazca habilitado
    
    # Lo enviamos a la capa de datos para guardar
    resultado = guardar_trabajador(nuevo_trabajador)
    if resultado == 1:
        print(f'Se ha guardado el trabajador con ID: {nuevo_trabajador.id_trabajador}')