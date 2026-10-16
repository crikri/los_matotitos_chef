from datos.repositorio.repositorio_comunas import listado_comunas, guardar_comuna
from prettytable import PrettyTable
from datos.modelos.comuna import Comuna


def cargar_comunas(tabla: PrettyTable):
    comunas = listado_comunas()
    tabla.field_names = ["ID", "Codigo", "Comuna"]

    if comunas:
        for comuna in comunas:
            # USAMOS TUS ATRIBUTOS CORRECTOS AQUÍ:
            tabla.add_row(
                [comuna.id_comuna, comuna.codigo_comuna, comuna.comuna])

    return tabla


def crear_comuna(codigo, nombre):
    nueva_comuna = Comuna()
    # Asignamos los datos al objeto
    nueva_comuna.codigo_comuna = codigo
    nueva_comuna.comuna = nombre

    # Lo mandamos a la capa de datos para que se guarde en la BD
    comuna_guardada = guardar_comuna(nueva_comuna)
    return comuna_guardada