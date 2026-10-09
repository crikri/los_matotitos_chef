from datos.conexion import conectar_db
from peewee import Model, CharField, AutoField, IntegerField
database = conectar_db()


class BaseModel(Model):
    class Meta:
        database = database


class Direccion(BaseModel):
    calle = CharField(max_length=50)
    comuna = IntegerField(index=True)
    departamento = CharField(max_length=10, null=True)
    id_direccion = AutoField()
    numero = CharField(max_length=10)

    class Meta:
        table_name = 'direcciones'