from datos.conexion import conectar_db
from datos.modelos.direccion import Direccion
from peewee import Model, CharField, IntegerField, AutoField, DateField
database = conectar_db()


class BaseModel(Model):
    class Meta:
        database = database


class Cliente(BaseModel):
    id_cliente = AutoField()
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
    direccion = IntegerField(index=True)
    email = CharField(max_length=50)
    fecha_nacimiento = DateField()
    nacionalidad = IntegerField(index=True)
    telefono = CharField(max_length=12)

    class Meta:
        table_name = "clientes"