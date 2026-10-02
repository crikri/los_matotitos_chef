from presentacion import menu_principal
from datos.repositorio.repositorio_clientes import guardar_cliente
from datos.modelos.clientes import Cliente
menu_principal()

cliente = Cliente(nombre = "matoto", telefono = "999999999", nacionalidad = "Chile", fecha_nacimiento = "2004-4-5",
                       email = "djadjaj@gmail.com",
                       direccion = "matoto_house",
                       apellido = "matoto")
guardar_cliente(cliente)