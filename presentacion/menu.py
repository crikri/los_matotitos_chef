import sys
from datos import nombre_app, version_app, main_menu
from presentacion.presentacion_comunas import datos_comuna, mostrar_comunas, buscar_comuna_nombre, eliminar_comuna


def menu_principal():
    print(f'{nombre_app} {version_app}')
    print('='*len(nombre_app) + "=" + '='*len(version_app))

    while True:
        for clave, valor in main_menu.items():
            print(f'[{clave}] - {valor}')

        opcion_usuario = input('Ingrese una opción [1-5]: ')

        if opcion_usuario == '1':
            mostrar_comunas()
        elif opcion_usuario == '2':
            datos_comuna()
        elif opcion_usuario == '3':
            nombre = input("Ingrese nombre de comuna a buscar: ")
            buscar_comuna_nombre(nombre)
        elif opcion_usuario == '4':
            eliminar_comuna()
        elif opcion_usuario == '5':
            print('Saliendo de Sistema')
            sys.exit()
        else:
            print('Opción Ingresada NO corresponde...\nIngrese nuevamente.')
