from datos.auxiliar import (
    nombre_app,
    version_app,
    main_menu,
    menu_restaurantes_dict,
    menu_comunas_dict,
    menu_mesas_dict,
    menu_reservas_dict,
    menu_trabajadores_dict

)

# Importamos las funciones de Restaurantes
from presentacion.presentacion_restaurantes import (
    mostrar_restaurantes,
    datos_restaurante_crear,
    eliminar_restaurante,
    actualizar_restaurante
)

# Importamos las funciones de Comunas que ya tienes listas
from presentacion.presentacion_comunas import (
    mostrar_comunas,
    datos_comuna_crear,
    buscar_comuna_nombre,  # o el nombre que tenga tu función de búsqueda
    eliminar_comuna
)
from presentacion.presentacion_mesas import (
    mostrar_mesas,
    datos_mesa_crear,
    actualizar_mesa,
    eliminar_mesa
)

# Importamos las funciones de Reservas
from presentacion.presentacion_reservas import (
    mostrar_reservas,
    datos_reserva_crear,
    eliminar_reserva
)

# Importamos las funciones de Trabajadores
from presentacion.presentacion_trabajador import (
    mostrar_trabajadores,
    datos_trabajador_crear,
    eliminar_trabajador
)


def dibujar_menu(titulo, opciones):
    """Imprime el marco visual del menú usando el diccionario correspondiente."""
    print("\n" + "=" * 45)
    print(f"   {nombre_app.upper()} - {titulo.upper()}")
    print("=" * 45)
    for clave, texto in opciones.items():
        print(f"[{clave}] - {texto}")
    print("=" * 45)


def sub_menu_restaurantes():
    while True:
        dibujar_menu("Gestión de Restaurantes", menu_restaurantes_dict)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_restaurantes()
        elif opcion == "2":
            datos_restaurante_crear()
        elif opcion == "3":
            actualizar_restaurante()
        elif opcion == "4":
            eliminar_restaurante()
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def sub_menu_comunas():
    while True:
        dibujar_menu("Gestión de Comunas", menu_comunas_dict)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_comunas()
        elif opcion == "2":
            datos_comuna_crear()
        elif opcion == "3":
            nombre = input("Ingrese nombre de comuna a buscar: ")
            buscar_comuna_nombre(nombre)
        elif opcion == "4":
            eliminar_comuna()
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def sub_menu_mesas():
    while True:
        dibujar_menu("Gestión de Mesas", menu_mesas_dict)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_mesas()
        elif opcion == "2":
            mostrar_mesas()
            datos_mesa_crear()
        elif opcion == "3":
            actualizar_mesa()
        elif opcion == "4":
            eliminar_mesa()
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def menu_principal():
    while True:
        dibujar_menu(f"Menú Principal ({version_app})", main_menu)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            sub_menu_restaurantes()
        elif opcion == "2":
            sub_menu_comunas()
        elif opcion == "3":
            sub_menu_mesas()
        elif opcion == "4":
            sub_menu_reservas()
        elif opcion == "5":
            sub_menu_trabajadores()
        elif opcion == "0":
            print(f"\nSaliendo de {nombre_app}... ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def sub_menu_reservas():
    while True:
        dibujar_menu("Gestión de Reservas", menu_reservas_dict)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_reservas()
        elif opcion == "2":
            datos_reserva_crear()
        elif opcion == "4":
            eliminar_reserva()
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")


def sub_menu_trabajadores():
    while True:
        dibujar_menu("Gestión de Trabajadores", menu_trabajadores_dict)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_trabajadores()
        elif opcion == "2":
            datos_trabajador_crear()
        elif opcion == "4":
            eliminar_trabajador()
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")
