from datos.conexion import conectar_db
from peewee import BooleanField, Model, CharField, IntegerField, AutoField
database = conectar_db()


class BaseModel(Model):
    class Meta:
        database = database


class Restaurante(BaseModel):
    direccion = IntegerField(index=True)
    email = CharField(max_length=50)
    id_restaurantes = AutoField()
    nombre = CharField(max_length=50)
    telefono = CharField(max_length=12)
    website = CharField(max_length=50, null=True)
    habilitado = BooleanField()

    class Meta:
        table_name = 'restaurantes'
