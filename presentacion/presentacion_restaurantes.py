from prettytable import PrettyTable
from datos.repositorio.respositorio_restaurantes import restaurante_por_id, guardar_restaurante
from negocio.negocio_restaurantes import cargar_restaurantes, registrar_nuevo_restaurante, eliminar_restaurante_logico


def mostrar_restaurantes():
    tabla_restaurantes = PrettyTable()
    tabla_restaurantes = cargar_restaurantes(tabla_restaurantes)
    print(tabla_restaurantes)


def datos_restaurante_crear():
    print("\n--- REGISTRAR NUEVO RESTAURANTE ---")
    nombre = input("Ingrese nombre: ").strip()
    direccion = input("Ingrese código/número de dirección: ").strip()
    email = input("Ingrese email: ").strip()
    telefono = input("Ingrese teléfono: ").strip()
    website = input("Ingrese sitio web (o ENTER para omitir): ").strip()

    exito = registrar_nuevo_restaurante(
        nombre, direccion, email, telefono, website)
    if exito:
        print(f"Restaurante '{nombre}' registrado con éxito.")
    else:
        print("No se pudo registrar el restaurante.")


def actualizar_restaurante():
    print("\n--- MODIFICAR RESTAURANTE ---")
    mostrar_restaurantes()

    id_ingresado = input(
        "Ingrese ID de restaurante para modificar (o ENTER para cancelar): ").strip()
    if not id_ingresado:
        return

    if not id_ingresado.isdigit():
        print("El ID debe ser un número entero válido.")
        return

    restaurante = restaurante_por_id(id_ingresado)
    if not restaurante:
        print(f"No se encontró restaurante con ID {id_ingresado}.")
        return

    print(
        f"\nModificando: {restaurante.nombre} (Presione ENTER para conservar el valor actual)")
    nombre_nuevo = input(f"Nuevo nombre [{restaurante.nombre}]: ").strip()
    direccion_nueva = input(
        f"Nueva dirección [{restaurante.direccion}]: ").strip()
    email_nuevo = input(f"Nuevo email [{restaurante.email}]: ").strip()
    telefono_nuevo = input(
        f"Nuevo teléfono [{restaurante.telefono}]: ").strip()
    website_nuevo = input(
        f"Nuevo sitio web [{restaurante.website or 'N/A'}]: ").strip()

    if nombre_nuevo != '':
        restaurante.nombre = nombre_nuevo
    if direccion_nueva != '' and direccion_nueva.isdigit():
        restaurante.direccion = int(direccion_nueva)
    if email_nuevo != '':
        restaurante.email = email_nuevo
    if telefono_nuevo != '':
        restaurante.telefono = telefono_nuevo
    if website_nuevo != '':
        restaurante.website = website_nuevo

    respuesta = guardar_restaurante(restaurante)
    if respuesta is not None:
        print("Restaurante actualizado correctamente.")
    else:
        print("No se pudo actualizar el restaurante.")


def eliminar_restaurante():
    print("\n" + "=" * 40)
    print("      ELIMINAR RESTAURANTE")
    print("=" * 40)

    # Mostramos la lista primero para ver los IDs disponibles
    mostrar_restaurantes()

    entrada = input(
        "Ingrese el ID del restaurante que desea eliminar (o presione Enter para cancelar): ").strip()
    if not entrada:
        print("Operación cancelada.")
        return

    exito = eliminar_restaurante_logico(entrada)
    if exito:
        print(f"\n¡Restaurante con ID {entrada} eliminado con éxito!")
    else:
        print("\nNo se pudo eliminar el restaurante.")
