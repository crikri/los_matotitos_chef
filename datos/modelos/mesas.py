from datos.conexion import conectar_db
from peewee import Model, CharField, IntegerField, AutoField, DateField
database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class mesas(BaseModel):
    id_mesas = AutoField()
    capacidad = IntegerField()
    estado = CharField(max_length=1)
    restaurante = IntegerField(index=True)
    numero_mesa = CharField(max_length=5)

    class Meta:
        table_name = "mesas"
        