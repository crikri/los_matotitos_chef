from datos.conexion import conectar_db
from peewee import Model, CharField, IntegerField, AutoField, DateField
database = conectar_db()

class BadeModel(Model):
    class Meta:
        detabase = database

class Direcciones(BadeModel):
    id_direccion = AutoField()
    calle = CharField(max_length=50)
    numero = CharField(max_length=10)
    departamento = CharField(max_length=10, null=True)
    comuna = IntegerField(index=True)

    class Meta:
        table_name = "direcciones"