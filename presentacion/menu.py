from datos.auxiliar import (
    nombre_app,
    version_app,
    main_menu,
    menu_restaurantes_dict,
    menu_comunas_dict
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


def menu_principal():
    while True:
        dibujar_menu(f"Menú Principal ({version_app})", main_menu)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            sub_menu_restaurantes()
        elif opcion == "2":
            sub_menu_comunas()
        elif opcion == "0":
            print(f"\nSaliendo de {nombre_app}... ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
