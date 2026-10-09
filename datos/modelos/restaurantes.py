from datos.conexion import conectar_db
from peewee import Model, CharField, IntegerField, AutoField, DateField
database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Restaurantes(BaseModel):
    id_restaurante = AutoField()
    nombre = CharField(max_length=50)
    direccion = IntegerField(index=True)
    telefono = Charfield(max_length=12)
    email = CharField(max_length=50)
    website = CharField(max_length=50, null=True)

    class Meta:
        table_name = "restaurantes"


s