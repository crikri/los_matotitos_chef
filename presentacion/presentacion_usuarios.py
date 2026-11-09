import re
import pwinput
import bcrypt
from datos.modelos.usuario import Usuario
from auxiliar.auxiliar import nombre_app, version_app
from auxiliar.validaciones import validar_rut, validar_correo
from negocio.negocio_usuarios import registrar_nuevo_usuario, cargar_usuarios
from negocio.negocio_paises import buscar_pais, obtener_id_pais_valido
from datos.repositorio.repositorio_usuarios import usuario_por_correo
from prettytable import PrettyTable
from presentacion.menu import menu_principal


def menu_agregar_usuario():
    rut = ""
    print("\n--- REGISTRAR NUEVO USUARIO ---")
    while rut == "":
        rut = input("RUT (Ej: 12345678-9): ")
        if not validar_rut(rut):
            print("RUT inválido. Intente nuevamente.")
            rut = ""


def mostrar_usuarios():
    tabla_usuarios = PrettyTable()
    tabla_usuarios = cargar_usuarios(tabla_usuarios)
    print(tabla_usuarios)


def datos_usuario():
    try:
        rut = nombre = apellido = correo = nombre_pais = fecha_nacimiento = genero = contrasenia = ''
        print('\nIngrese Datos Usuario')

        while rut == '':
            rut = input('RUT: ')
            if not validar_rut(rut):
                print('RUT NO corresponde, ingrese nuevamente...')
                rut = ''
        while nombre == '':
            nombre = input('Nombre: ')
        while apellido == '':
            apellido = input('Apellido: ')
        while correo == '':
            correo = input('Correo: ')
            correo = validar_correo(correo)

        id_pais = None
        while id_pais is None:
            nombre_pais = input('Nombre País: ').strip()
            if nombre_pais == '':
                continue
            tabla_paises = PrettyTable()
            tabla_paises = buscar_pais(tabla_paises, nombre_pais)
            if not tabla_paises.rows:
                print('No se encontraron países con ese nombre, intente nuevamente...')
                continue
            print(tabla_paises)

            # Se guarda el id elegido de la tabla (no el nombre)
            id_pais = obtener_id_pais_valido(
                input('Id País (según la tabla): '))
            if id_pais is None:
                print('Id de país NO válido, busque nuevamente...')

        while fecha_nacimiento == '':
            fecha_nacimiento = input('Fecha Nacimiento (dd/MM/aaaa): ')

        while genero == '':
            print('Opciones de Género')
            print('[1] Masculino')
            print('[2] Femenino')
            print('[3] Otro')
            genero = input('Opción Género [1-3]: ')
            if genero not in ['1', '2', '3']:
                print('Género NO corresponde, ingrese nuevamente...')
                genero = ''

        while contrasenia == '':
            patron_contrasenia = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){8,15}$'
            print('Ingrese una contraseña segura:')
            print('Al menos una minúscula\nAl menos una mayúscula\nAl menos un dígito\nAl menos un caracter especial')
            print('Al menos 8 caracteres de largo')
            contrasenia = pwinput.pwinput(prompt='Contraseña: ', mask='*')
            if not re.match(patron_contrasenia, contrasenia):
                print('Su contraseña NO es segura, ingrese nuevamente...')
                contrasenia = ''
        registrar_nuevo_usuario(rut, nombre.title(), apellido.title(
        ), correo, id_pais, fecha_nacimiento, genero, contrasenia)
    except Exception as e:
        print(f"Error al registrar usuario: {e}")


def login_usuario():
    correo = ""
    while correo == "":
        print(f"\n--- {nombre_app} v{version_app} ---")
        print("--- LOGIN USUARIO ---")
        print("Ingrese sus credenciales para iniciar sesión.")

        correo = input("Correo: ")
        if not validar_correo(correo):
            print("Correo inválido. Intente nuevamente.")
            correo = ""
        else:
            usuario = usuario_por_correo(correo)

            if usuario:
                contrasenia = input("Contraseña: ")
                if not bcrypt.checkpw(contrasenia.encode('utf-8'), usuario.password.encode('utf-8')):
                    print("Contraseña incorrecta. Intente nuevamente.")
                    correo = ""
                elif bcrypt.checkpw(contrasenia.encode('utf-8'), usuario.password.encode('utf-8')):
                    print(f"Bienvenido, {usuario.nombre} {usuario.apellido}!")
                    menu_principal()
            if not usuario:
                print("Usuario no encontrado, desea registrarse? (s/n)")
                opcion = input().lower()
                match opcion.lower():
                    case "s":
                        datos_usuario()
                    case "n":
                        correo = ""
