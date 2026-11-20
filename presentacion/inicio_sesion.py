from datos.modelos.usuario import Usuario
import bcrypt
import pwinput
from auxiliar.auxiliar import nombre_app, version_app
from auxiliar.validaciones import validar_correo
from presentacion.menu import menu_principal
from presentacion.presentacion_usuarios import datos_usuario


def login_usuario():
    """Retorna el Usuario autenticado, o None si se cancela o falla el acceso."""
    while True:
        print(f"{nombre_app} {version_app}")
        print("=" * len(nombre_app) + "=" + "=" * len(version_app))
        print("Ingrese sus credenciales para iniciar sesión.")

        correo = " "
        while correo == " ":
            correo = input("Correo: ")
            if not validar_correo(correo):
                print("Correo inválido. Intente nuevamente.")
                correo = " "

        usuario = Usuario.get_or_none(Usuario.email == correo)

        if usuario is not None:
            if not usuario.habilitado:
                print("Este usuario está deshabilitado.\n")
                continue

            for intento in range(3):
                contrasenia = pwinput.pwinput(prompt='Contraseña: ', mask='*')
                if usuario.password and bcrypt.checkpw(
                        contrasenia.encode('utf-8'),
                        usuario.password.encode('utf-8')):
                    print(f"\nBienvenido, {usuario.nombre}.\n")
                    menu_principal()
                    break
                else:
                    print(
                        f"Contraseña incorrecta. Intentos restantes: {2 - intento}")
        if usuario is None:
            print("Usuario no encontrado. \n¿Desea registrarse?")
            opcion_registro = input("Ingrese Si/No [s-n]: ")

            match opcion_registro.lower():
                case "s":
                    datos_usuario()
                case "n":
                    print("No se creara usuario...")
        print(f"\n¿Desea salir del programa?")
        opcion_salida = input("Ingrese Si/No [s-n]: ")
        match opcion_salida.lower():
            case "s":
                print("Saliendo del programa...")
                break
            case "n":
                continue


def solicitar_correo():
    correo = mensaje = ""
    while correo == "":
        correo = input("Ingrese su correo electrónico: ")
        if validar_correo(correo):
            mensaje = "Correo electronico."
        else:
            correo = ""
    return correo, mensaje
