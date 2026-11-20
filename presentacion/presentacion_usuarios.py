import re
import pwinput
from prettytable import PrettyTable
from negocio.negocio_paises import buscar_pais, obtener_id_pais_valido
from negocio.negocio_usuarios import registrar_nuevo_usuario
from auxiliar.validaciones import validar_rut, validar_correo
from negocio.negocio_usuarios import cargar_usuarios
from negocio.negocio_paises import buscar_pais, obtener_id_pais_valido
from auxiliar.validaciones import validar_correo, validar_rut

from prettytable import PrettyTable


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
            patron_contrasenia = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@!%*?&#._-])[A-Za-z\d$@!%*?&#._-]{8,}\Z'
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


def actualizar_datos_usuario():
    rut = nombre = apellido = correo = nombre_pais = fecha_nacimiento = genero = ''
    print('\nIngrese Nuevos Datos de Usuario')
    print('Introduzca nuevos datos para actualizar\no Enter para conservar.')

    while rut == '':
        rut = input('RUT del usuario a modificar (12.345.678-5): ')
        if not validar_rut(rut):
            print('Rut NO VÁLIDO, ingrese nuevamente...')
            rut = ''
        else:
            usuario = usuario_por_rut(rut)

    if usuario:
        print('Usuario encontrado.')

        nombre = input('Nombre (o Enter para conservar): ')
        apellido = input('Apellido (o Enter para conservar): ')
        correo = input('Correo (o Enter para conservar): ')
        if not validar_correo(correo):
            print('Correo electrónico NO corresponde, no será modificado...')
            correo = ''

        nombre_pais = input('Nombre País (o Enter para conservar): ')
        id_pais = ''
        if nombre_pais != '':
            tabla_paises = PrettyTable()
            tabla_paises = buscar_pais(tabla_paises, nombre_pais)
            print(tabla_paises)
            id_pais = obtener_id_pais_valido(input('Id País: '))
            if id_pais is None:
                print('Id de país NO válido, no será modificado...')
                id_pais = ''

        fecha_nacimiento = input(
            'Fecha Nacimiento (dd/MM/aaaa) (o Enter para conservar): ')
        if not validar_fecha(fecha_nacimiento):
            print('Fecha NO válida, no será modificada...')
            fecha_nacimiento = ''

        print('Opciones de Género')
        print('[1] Masculino')
        print('[2] Femenino')
        print('[3] Otro')
        genero = input('Opción Género [1-3]: ')
        if not validar_genero(genero):
            print('Género NO corresponde, no será modificado...')
            genero = ''

        modificar_usuario(rut, nombre.title(), apellido.title(), correo,
                          id_pais, fecha_nacimiento, genero, usuario)
    else:
        print('Usuario no encontrado.')


def deshabilitar_usuario():
    rut = ""
    print("\nIngrese nuevos datos de usuario")
    print("\nIngrese nuevos datos para actualizar\no Enter para conservar.")

    while rut == "":
        rut = input("RUT (12.345.678-5) (o enter para conservar): ")
        if not validar_rut(rut):
            print("RUT inválido. Intente nuevamente.")
            rut = ""
        else:
            usuario = usuario_por_rut(rut)

            if usuario:
                print(f"Usuario encontrado.")
                print(
                    f"¿Estas seguro que deseas deshabilitar al usuario {usuario.nombre} {usuario.apellido}?")
                if opcion.lower == "s":
                    usuario.habilitado = False
                    usuario.save()

                    modificar_usuario("", "", "", "", "", "", "", usuario)
