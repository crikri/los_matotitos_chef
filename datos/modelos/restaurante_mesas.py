from datos.conexion import conectar_db
from peewee import Model, CharField, IntegerField, AutoField, DateField
database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class restaurante_mesas(BaseModel):
    id_restaurante_mesas = AutoField()
    restaurante = IntegerField(index=True)
    mesa = IntegerField(index=True)

    class Meta:
        table_name = "restaurante_mesas"
        