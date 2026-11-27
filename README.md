Nombre del proyecto: Gestion de restaurante
Integrantes:
-Fernando Medina
-Cristobal Nawrath
-Diego Barrales

Descripción general.
-Es un sistema de gestion de reservas, mesas, restaurantes y usuarios 
que como proposito tiene el facilitar la gestion de las reservas de 
mesas a el restaurante cocmo a los clientes

Dependencias.

bcrypt==5.0.0
mysql-connector-python==9.7.0
mysqlclient==2.2.8
peewee==4.5.1
prettytable==3.17.0
pwinput==1.0.3
PyMySQL==1.2.3
rut-chile==2.0.1
python-decouple==3.8
prettytable==3.17.0

Procedimiento de instalación.

El procedimiento para instalar es ejecuyar el ddl,
que esta dentro de datos/sql, posterior realizar los inserts de comunas 
y insert de paises, ejecutar los privilegios.

IMPORTANTE: Instalar las deendencias del archivo requirements.txt, sino
no se podra realizar la comunicacion ni con el orm ni ejecutar
ciertas funciones

Procedimiento de creación de base de datos.

Se usa los archivos de:
-Ddl_restaurante
-Insert_comunas
-Insert_paises
-Privilegios

Usuario inicial (si corresponde).


Instrucciones de ejecución.

El usuario para ingresar al sistema se crea desde el mismo menu,
se debe de ingresar un correo valido com por ej: "hola@gmail.com",
con ello el sistema comprobara que no existe en la base de datos y
habilitara la opcion de crear un usuario, con ese usuario se inicia sesion
de manera posterior