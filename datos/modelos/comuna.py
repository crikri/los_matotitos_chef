from datos.conexion import conectar_db
from peewee import BooleanField, Model, CharField, AutoField
database = conectar_db()


class BaseModel(Model):
    class Meta:
        database = database


class Comuna(BaseModel):
    codigo_comuna = CharField(max_length=5)
    comuna = CharField(max_length=30)
    id_comuna = AutoField()
    habilitado = BooleanField()

    class Meta:
        table_name = 'comunas'
