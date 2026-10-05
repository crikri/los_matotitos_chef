from datos.repositorio import repositorio_paises
from presentacion import menu_principal
from datos.repositorio.repositorio_clientes import guardar_cliente
from datos.modelos.cliente import Cliente
from datos.repositorio import repositorio_paises
from prettytable import PrettyTable
# menu_principal()

cliente = Cliente(nombre="matoto", telefono="999999999", nacionalidad="Chile", fecha_nacimiento="2004-4-5",
                  email="djadjaj@gmail.com",
                  direccion="matoto_house",
                  apellido="matoto")
guardar_cliente(cliente)

listado_paises = repositorio_paises.listado_paises()

tabla_paises = PrettyTable()
tabla_paises.field_names = ["ID", "ISO_2", "ISO_3", "Nacionalidad", "Nombre"]
for pais in listado_paises:
    tabla_paises.add_row([pais.id_pais, pais.iso_2, pais.iso_3, pais.nacionalidad, pais.nombre])
print(tabla_paises)