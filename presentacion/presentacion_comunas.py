from negocio.negocio_comunas import cargar_comunas
from prettytable import PrettyTable


def mostrar_comunas():
    tabla_comunas = PrettyTable()
    tabla_comunas = cargar_comunas(tabla_comunas)
    print(tabla_comunas)

--

def datos_comuna ()
    codigo = input("Ingrese codigo de comuna: ")
    nombre = input("Ingrese nombre de comuna: ")
    crear_comuna(codigo, nombre)

def buscar_comuna_nombre(nombre):
    tabla_comunas PrettyTable()
    tabla_comunas = buscar_comunas(tabla, columna, nombre)
    print(tabla_comunas)

def datos_actualizar_comunas()
    nombre = input("Ingrese nombre de comuna: ")
    buscar_comuna_nombre(nombre)
    id_ingresado = input("Ingrese Id de comuna para modificar:")
    comuna = comuna_por_id(id)
    nombre_nuevo = input ("Ingrese nuevo nombre de comuna (o ENTER para conservar:)")
    codigo_nuevo = input ("Ingrese nuevo codigo de comuna (o ENTER para conservar:)")

    if nombre_nuevo != '':
        comuna.comuna = nombre_nuevo.title()
    if codigo_nuevo != '':
        comuna.codigo_comuna = codigo_nuevo
        respuesta 
        
    
