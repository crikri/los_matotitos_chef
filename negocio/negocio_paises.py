from prettytable import PrettyTable
from datos.modelos.pais import Pais
from datos.repositorio.repositorio_paises import obtener_pais_nombre, obtener_pais_id


def buscar_pais(tabla: PrettyTable, nombre):
    tabla.field_names = [
        "Id",
        "Nombre",
        "Nacionalidad",
        "ISO 2",
        "ISO 3"
    ]

    paises = obtener_pais_nombre(nombre)

    if paises:
        for pais in paises:
            tabla.add_row([
                pais.id_pais,
                pais.nombre,
                pais.nacionalidad,
                pais.iso_2,
                pais.iso_3
            ])

    return tabla


def obtener_id_pais_valido(texto_id):
    """Devuelve el id (int) si el texto es un número y el país existe; si no, None."""
    if not texto_id.strip().isdigit():
        return None
    pais = obtener_pais_id(int(texto_id))
    return pais.id_pais if pais else None