from negocio.negocio_comunas import obtener_datos_comuna
from negocio.negocio_comunas import cargar_comunas, crear_comuna, buscar_comunas, obtener_datos_comuna
from prettytable import PrettyTable
from datos.repositorio.repositorio_comunas import comuna_por_id, guardar_comuna


def mostrar_comunas():
    tabla_comunas = PrettyTable()
    tabla_comunas = cargar_comunas(tabla_comunas)
    print(tabla_comunas)


def datos_comuna_crear():
    codigo = input("Ingrese codigo de comuna: ")
    nombre = input("Ingrese nombre de comuna: ")
    crear_comuna(codigo, nombre)


def buscar_comuna_nombre(nombre):
    tabla_comunas = PrettyTable()
    tabla_comunas = buscar_comunas(tabla_comunas, nombre)
    print(tabla_comunas)


def actualizar_comuna():
    nombre = input("Ingrese nombre de comuna: ")
    buscar_comuna_nombre(nombre)
    id_ingresado = input("Ingrese Id de comuna para modificar:")
    comuna = comuna_por_id(id_ingresado)
    nombre_nuevo = input(
        "Ingrese nuevo nombre de comuna (o ENTER para conservar:)")
    codigo_nuevo = input(
        "Ingrese nuevo codigo de comuna (o ENTER para conservar:)")

    if nombre_nuevo != '':
        comuna.comuna = nombre_nuevo
    if codigo_nuevo != '':
        comuna.codigo_comuna = codigo_nuevo
    respuesta = guardar_comuna(comuna)
    if respuesta == 1:
        print("Comuna actualizada correctamente")


def eliminar_comuna():
    nombre = input('Ingrese Nombre de Comuna: ')
    buscar_comuna_nombre(nombre)

    entrada = input('Ingrese Id de Comuna para eliminar: ')
    if not entrada.isdigit():
        print('El ID debe ser un número entero válido.')
        return

    comuna = comuna_por_id(entrada)
    if not comuna:
        print(f'No se encontró la comuna con ID {entrada}.')
        return

    # Cambiar estado y guardar
    comuna.habilitado = False
    respuesta = guardar_comuna(comuna)

    if respuesta == 1:
        print(f'Comuna {comuna.comuna} eliminada con éxito.')
    else:
        print('No se pudo actualizar el estado de la comuna.')


def datos_comuna(nombre):
    tabla_comunas = PrettyTable()
    tabla_comunas = buscar_comunas(tabla_comunas, nombre)
    print(tabla_comunas)

    print("\n--- CONSULTAR DATOS DE COMUNA ---")
    entrada = input("Ingrese el ID de la comuna: ")

    if not entrada.isdigit():
        print("El ID debe ser un número entero válido.")
        return

    comuna = obtener_datos_comuna(entrada)

    if not comuna:
        print(f"No se encontró ninguna comuna con el ID {entrada}.")
        return

    # Determinamos el estado legible
    estado = "Habilitada" if getattr(
        comuna, 'habilitado', True) else "Deshabilitada"

    print("\n================================")
    print(f" ID        : {comuna._pk}")
    print(f" Nombre    : {comuna.comuna}")
    print(f" Estado    : {estado}")

    # Si tu modelo tiene relación con provincia o región (Foreign Key), puedes mostrarla así:
    if hasattr(comuna, 'id_provincia') and comuna.id_provincia:
        # Si tiene relación directa en Peewee: comuna.id_provincia.nombre_provincia
        print(f" Provincia : {comuna.id_provincia}")

    print("================================\n")
