from peewee import *
from datos.conexion import conectar_db
database = conectar_db()
defecto = "DEFAULT 1"






class RestauranteMesas(BaseModel):
    id_restaurante_mesa = AutoField()
    mesa = IntegerField(index=True)
    restaurante = IntegerField(index=True)

    class Meta:
        table_name = 'restaurante_mesas'

class Restaurantes(BaseModel):
    direccion = IntegerField(index=True)
    email = CharField(max_length=50)
    id_restaurantes = AutoField()
    nombre = CharField(max_length=50)
    telefono = CharField(max_length=12)
    website = CharField(max_length=50, null=True)

    class Meta:
        table_name = 'restaurantes'

class RestaurantesHorarios(BaseModel):
    horario = IntegerField(index=True)
    id_restaurante_horario = AutoField()
    restaurante = IntegerField(index=True)

    class Meta:
        table_name = 'restaurantes_horarios'

class RestaurantesTrabajadores(BaseModel):
    id_restaurante_trabajador = AutoField()
    restaurante = IntegerField(index=True)
    trabajador = IntegerField(index=True)

    class Meta:
        table_name = 'restaurantes_trabajadores'

