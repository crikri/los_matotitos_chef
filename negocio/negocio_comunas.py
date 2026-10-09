from datos.repositorio.repositorio_comunas import listado_comunas
from prettytable import PrettyTable
def listado_comunas(tabla : PrettyTable):
    comunas = listado_comunas()
    tabla.field_names = ["ID", "Codigo", "Comuna"]

    if comunas:
        for comuna in comunas:
            tabla.add_row([comuna.id_comuna, comuna.codigo, comuna.nombre])