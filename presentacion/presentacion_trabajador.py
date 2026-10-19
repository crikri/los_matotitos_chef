from negocio.negocio_trabajador import cargar_trabajadores, crear_trabajador
from prettytable import PrettyTable
from datos.repositorio.repositorio_trabajador import trabajador_por_id, guardar_trabajador

def mostrar_trabajadores():
    tabla = PrettyTable()
    tabla = cargar_trabajadores(tabla)
    print("\n--- LISTA DE TRABAJADORES ---")
    print(tabla)

def datos_trabajador_crear():
    print("\n--- REGISTRAR NUEVO TRABAJADOR ---")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    nacionalidad = input("ID de Nacionalidad: ")
    direccion = input("ID de Dirección: ")
    telefono = input("Teléfono: ")
    
    crear_trabajador(nombre, apellido, fecha_nacimiento, nacionalidad, direccion, telefono)

def eliminar_trabajador():
    print("\n--- ELIMINAR TRABAJADOR ---")
    entrada = input('Ingrese ID del Trabajador para eliminar (Lógico): ')
    
    if not entrada.isdigit():
        print('El ID debe ser un número.')
        return

    trabajador = trabajador_por_id(entrada)
    if not trabajador:
        print(f'No se encontró el trabajador con ID {entrada}.')
        return

    # Se aplica el borrado lógico
    trabajador.habilitado = False
    if guardar_trabajador(trabajador) == 1:
        print('Trabajador eliminado con éxito.')