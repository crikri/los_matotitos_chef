from prettytable import PrettyTable
from negocio.negocio_clientes import cargar_clientes, crear_cliente
from datos.repositorio.repositorio_clientes import cliente_por_rut, guardar_cliente
from auxiliar.validaciones import validar_rut, validar_correo, normalizar_rut


def mostrar_clientes():
    tabla = PrettyTable()
    tabla = cargar_clientes(tabla)
    print("\n--- LISTA DE CLIENTES ---")
    print(tabla)


def datos_cliente_crear(rut=None):
    """Registra un cliente. Si viene el rut (ya validado) no lo vuelve a pedir.
    Retorna el Cliente creado, o None si no se pudo crear."""
    nombre = apellido = telefono = correo = ''
    print("\n--- REGISTRAR NUEVO CLIENTE ---")

    while rut is None:
        rut = input("RUT (12.345.678-5): ")
        if not validar_rut(rut):
            print("RUT NO VÁLIDO, ingrese nuevamente...")
            rut = None
    rut = normalizar_rut(rut)

    if cliente_por_rut(rut):
        print("Ya existe un cliente con ese RUT.")
        return None

    while nombre == '':
        nombre = input("Nombre: ").strip()
    while apellido == '':
        apellido = input("Apellido: ").strip()
    while telefono == '' or len(telefono) > 12:
        telefono = input("Teléfono (máx. 12 caracteres): ").strip()
    while correo == '':
        correo = validar_correo(input("Correo: ").strip())

    return crear_cliente(rut, nombre.title(), apellido.title(), telefono, correo)


def modificar_cliente():
    print("\n--- MODIFICAR CLIENTE ---")
    rut = input("RUT del cliente a modificar: ")
    if not validar_rut(rut):
        print("RUT NO VÁLIDO.")
        return

    cliente = cliente_por_rut(normalizar_rut(rut))
    if not cliente:
        print("Cliente no encontrado.")
        return

    print(f"Cliente encontrado: {cliente.nombre} {cliente.apellido}")
    nombre = input("Nombre (o ENTER para conservar): ").strip()
    apellido = input("Apellido (o ENTER para conservar): ").strip()
    telefono = input("Teléfono (o ENTER para conservar): ").strip()
    correo = input("Correo (o ENTER para conservar): ").strip()

    if nombre != '':
        cliente.nombre = nombre.title()
    if apellido != '':
        cliente.apellido = apellido.title()
    if telefono != '':
        if len(telefono) <= 12:
            cliente.telefono = telefono
        else:
            print("Teléfono demasiado largo, no será modificado...")
    if correo != '':
        if validar_correo(correo) != '':
            cliente.email = correo
        else:
            print("El correo no será modificado...")

    if guardar_cliente(cliente) == 1:
        print("Cliente actualizado correctamente")


def eliminar_cliente():
    print("\n--- ELIMINAR CLIENTE ---")
    rut = input("RUT del cliente a eliminar (Lógico): ")
    if not validar_rut(rut):
        print("RUT NO VÁLIDO.")
        return

    cliente = cliente_por_rut(normalizar_rut(rut))
    if not cliente:
        print(f"No se encontró el cliente con RUT {rut}.")
        return

    cliente.habilitado = False
    if guardar_cliente(cliente) == 1:
        print("Cliente eliminado con éxito.")


def seleccionar_cliente():
    """Pide un RUT y retorna el id_cliente. Si no existe, ofrece registrarlo.
    Retorna None si el usuario cancela (se usa al crear/modificar reservas)."""
    while True:
        rut = input("RUT del Cliente (12.345.678-5): ")
        if not validar_rut(rut):
            print("RUT NO VÁLIDO, ingrese nuevamente...")
            continue

        rut = normalizar_rut(rut)
        cliente = cliente_por_rut(rut)

        if cliente and cliente.habilitado:
            print(f"Cliente: {cliente.nombre} {cliente.apellido}")
            return cliente.id_cliente

        if cliente and not cliente.habilitado:
            print("Ese cliente está deshabilitado.")
            return None

        print("Cliente no registrado.\n¿Desea registrarlo?")
        opcion = input("Ingrese Si/No [s-n]: ").lower()
        if opcion == 's':
            nuevo = datos_cliente_crear(rut)
            if nuevo:
                return nuevo.id_cliente
        return None
