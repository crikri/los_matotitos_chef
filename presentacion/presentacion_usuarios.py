import getpass
from negocio.negocio_usuarios import registrar_nuevo_usuario, cargar_usuarios
from prettytable import PrettyTable

def mostrar_usuarios():
    tabla_usuarios = PrettyTable()
    tabla_usuarios = cargar_usuarios(tabla_usuarios)
    print(tabla_usuarios)

def menu_agregar_usuario():
    print("\n--- REGISTRAR NUEVO USUARIO ---")
    rut = input("RUT (Ej: 12345678-9): ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Correo electrónico: ") # <-- Variable ajustada
    
    try:
        pais = int(input("ID del País (Ej: 1 para Chile): "))
    except ValueError:
        pais = None

    fecha_nacimiento = input("Fecha de Nacimiento (YYYY-MM-DD) o presione Enter para omitir: ")
    
    print("\nOpciones de Género:")
    print("184: Masculino")
    print("185: Femenino")
    print("186: Otro")
    try:
        genero = int(input("Seleccione el ID de Género: "))
    except ValueError:
        genero = 186

    password = getpass.getpass("Contraseña (no se verá mientras escribes): ")

    exito = registrar_nuevo_usuario(
        rut, nombre, apellido, email, pais, fecha_nacimiento, genero, password
    )

    if exito:
        print("\nUsuario registrado correctamente.")
    else:
        print("\nHubo un problema al registrar el usuario.")