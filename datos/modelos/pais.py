from datos.conexion import conectar_db
from peewee import Model, CharField, AutoField
database = conectar_db()


class BaseModel(Model):
    class Meta:
        database = database


class Pais(BaseModel):
    id_pais = AutoField()
    iso_2 = CharField(max_length=2, null=True)
    iso_3 = CharField(max_length=3, null=True)
    nacionalidad = CharField(max_length=30)
    nombre = CharField(max_length=60)

    class Meta:
        table_name = "paises"
