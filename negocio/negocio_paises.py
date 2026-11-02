from prettytable import PrettyTable
from datos.modelos.pais import Pais
from datos.repositorio.repositorio_paises import obtener_paises_nombre_id

def buscar_pais(tabla: PrettyTable,nombre):
    pais = obtener_paises_nombre_id(nombre)
    tabla.fields = ["Id", "Nombre","Nacionalidad","ISO 2","ISO 3"]

    if pais:
        for paises in pais:
            tabla.add_row([pais.id, pais.nombre, pais.nacionalidad, pais.iso2, pais.iso3])

    return tabla
