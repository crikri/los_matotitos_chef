import re
from negocio.negocio_usuarios import registrar_nuevo_usuario, cargar_usuarios
from prettytable import PrettyTable

def mostrar_usuarios():
    tabla_usuarios = PrettyTable()
    tabla_usuarios = cargar_usuarios(tabla_usuarios)
    print(tabla_usuarios)
    id_pais = input("Ingrese el ID del país para filtrar usuarios (o presione Enter para mostrar todos): ")

    def datos_usuario():
        rut = nombre = apellido = correo = nombre_pais = fecha_nacimiento = genero = contrasenia = ''
        print('\nIngrese Datos Usuario')

    while rut == '':
        rut = input('RUT: ')
    while nombre == '':
        nombre = input('Nombre: ')
    while apellido == '':
        apellido = input('Apellido: ')
    while correo == '':
        correo = input('Correo: ')
        patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron_correo, correo):
            print('Correo electrónico NO corresponde, ingrese nuevamente...')
            correo = ''

    while fecha_nacimiento := input(""):
        fecha_nacimiento = input("Fecha de Nacimiento (dd-MM-aaaa): ")

    while genero == "":
        print("Opciones de Género:")
        print("[1]: Masculino")
        print("[2]: Femenino")
        print("[3]: Otro")
        genero = input("Seleccione el ID de Género [1-3]: ")
        if genero not in ["1", "2", "3"]:
            print("Género no corresponde. Ingrese nuevamente.")
            genero = ""
    
    while contrasenia == "":
        patron_contrasenia = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,15}$"
        print("Ingrese la contraseña (mínimo 8 caracteres, máximo 15, al menos una letra mayúscula, una letra minúscula, un número y un carácter especial): ")
        contrasenia = input("Contraseña: ")
        if not re.match(patron_contrasenia, contrasenia):
            print("Contraseña no cumple con los requisitos. Ingrese nuevamente.")
            contrasenia = ""

    crear_usuario(rut, nombre.title(), apellido.title(), correo, pais, fecha_nacimiento, genero, contrasenia)