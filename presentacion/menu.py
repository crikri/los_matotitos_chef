import sys
from datos.auxiliar import nombre_app, version_app

def menu_principal():
    print(f"{nombre_app} {version_app}")
    print("="*len(nombre_app) + "=" + "="*len(version_app))

    while True:
        print("[1] Gestión Restaurante")
        print("[2] Gestión Horario")
        print("[3] Gestión Reserva")
        print("[4] Salir del sistema")

        opcion_usuario = input("Ingrese una opción [1-4]: ")

        if opcion_usuario == "1":
            pass
        elif opcion_usuario == "2":
            pass
        elif opcion_usuario == "3":
            pass
        elif opcion_usuario == "4":
            print("Saliendo del sistema")
            sys.exit()
        else:
            print("La opción ingresada no corresponde...\nIngrese nuevamente")