from datetime import datetime
from negocio.negocio_trabajador import cargar_trabajadores, crear_trabajador
from prettytable import PrettyTable
from datos.repositorio.repositorio_trabajador import trabajador_por_id, guardar_trabajador
from negocio.negocio_paises import buscar_pais, obtener_id_pais_valido


def mostrar_trabajadores():
    tabla = PrettyTable()
    tabla = cargar_trabajadores(tabla)
    print("\n--- LISTA DE TRABAJADORES ---")
    print(tabla)


def datos_trabajador_crear():
    nombre_pais = ""
    print("\n--- REGISTRAR NUEVO TRABAJADOR ---")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    nacionalidad = None
    while nacionalidad is None:
        nombre_pais = input('Nombre País: ').strip()
        if nombre_pais == '':
            continue
        if nombre_pais == '':
            continue
        tabla_paises = PrettyTable()
        tabla_paises = buscar_pais(tabla_paises, nombre_pais)
        if not tabla_paises.rows:
            print('No se encontraron países con ese nombre, intente nuevamente...')
            continue
        print(tabla_paises)

        # Se guarda el id elegido de la tabla (no el nombre)
        nacionalidad = obtener_id_pais_valido(
            input('Id País (según la tabla): '))
        if nacionalidad is None:
            print('Id de país NO válido, busque nuevamente...')

    direccion = input("ID de Dirección: ")
    telefono = input("Teléfono: ")

    crear_trabajador(nombre, apellido, fecha_nacimiento,
                     nacionalidad, direccion, telefono)


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


def modificar_trabajador():
    mostrar_trabajadores()
    numero = input("Ingrese el id del trabajador")
    trabajador = trabajador_por_id(numero)

    nombre_nuevo = input("Ingrese nuevo nombre (o ENTER para conservar): ")
    apellido_nuevo = input("Ingrese nuevo apellido (o ENTER para conservar): ")
    fecha_nac_nueva = input(
        "Ingrese nueva fecha de nacimiento YYYY-MM-DD (o ENTER para conservar): ")
    nacionalidad_nueva = input(
        "Ingrese nuevo ID de nacionalidad (o ENTER para conservar): ")
    direccion_nueva = input(
        "Ingrese nuevo ID de dirección (o ENTER para conservar): ")
    telefono_nuevo = input("Ingrese nuevo teléfono (o ENTER para conservar): ")
    habilitado_nuevo = input(
        "¿Trabajador habilitado? (s/n o ENTER para conservar): ")

    if nombre_nuevo != '':
        trabajador.nombre = nombre_nuevo
    if apellido_nuevo != '':
        trabajador.apellido = apellido_nuevo
    if fecha_nac_nueva != '':
        trabajador.fecha_nacimiento = datetime.strptime(
            fecha_nac_nueva, "%Y-%m-%d").date()
    if nacionalidad_nueva != '':
        trabajador.nacionalidad = int(nacionalidad_nueva)
    if direccion_nueva != '':
        trabajador.direccion = int(direccion_nueva)
    if telefono_nuevo != '':
        trabajador.telefono = telefono_nuevo
    if habilitado_nuevo != '':
        trabajador.habilitado = habilitado_nuevo.lower() == 's'

    respuesta = guardar_trabajador(trabajador)

    if respuesta == 1:
        print("Comuna actualizada correctamente")

    # Aquí llamas a tu función de guardado
    # respuesta = guardar_trabajador(trabajador)
    # if respuesta == 1:
    #     print("Trabajador actualizado correctamente")
