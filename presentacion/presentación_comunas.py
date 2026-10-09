from negocio.negocio_comunas import listado_comunas
from prettytable import PrettyTable

def mostrar_comunas():
    tabla_comunas = PrettyTable()
    tabla_comunas = listado_comunas(tabla_comunas)
    print(tabla_comunas)
    