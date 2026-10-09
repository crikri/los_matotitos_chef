from datos.repositorio.repositorio_comunas import listado_comunas
from prettytable import PrettyTable
from datos.modelos.comuna import Comuna
from datos.repositorio.repositorio_comunas import guardar_comuna
def cargar_comunas(tabla : PrettyTable):
    comunas = listado_comunas()
    tabla.field_names = ["ID", "Codigo", "Comuna"]

    if comunas:
        for comuna in comunas:
            tabla.add_row([comuna.id_comuna, comuna.codigo, comuna.nombre])

        return tabla

def crear_comuna(codigo, nombre):
    nueva_comuna = Comuna()
    nueva_comuna.codigo_comuna = codigo
    nueva_comuna.comuna = nombre
    comuna = guardar_comuna(nueva_comuna)