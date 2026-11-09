import re
from auxiliar.validaciones import validar_rut, validar_correo
from negocio.negocio_usuarios import registrar_nuevo_usuario, cargar_usuarios  
from negocio.negocio_paises import buscar_pais, obtener_id_pais_valido
from prettytable import PrettyTable

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
        id_pais = obtener_id_pais_valido(input('Id País (según la tabla): '))
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
        if genero not in ['1','2','3']:
            print('Género NO corresponde, ingrese nuevamente...')
            genero = ''

    while contrasenia == '':
        patron_contrasenia = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){8,15}$'
        print('Ingrese una contraseña segura:')
        print('Al menos una minúscula\nAl menos una mayúscula\nAl menos un dígito\nAl menos un caracter especial')
        print('Al menos 8 caracteres de largo')
        contrasenia = input('Contraseña: ')
        if not re.match(patron_contrasenia, contrasenia):
            print('Su contraseña NO es segura, ingrese nuevamente...')
            contrasenia = ''
    registrar_nuevo_usuario(rut, nombre.title(), apellido.title(), correo, id_pais, fecha_nacimiento, genero, contrasenia)