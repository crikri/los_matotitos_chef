from datos.conexion import conectar_db
from peewee import BooleanField, Model, CharField, IntegerField, AutoField

database = conectar_db()


class BaseModel(Model):
    class Meta:
        database = database


class Mesa(BaseModel):
    id_mesa = AutoField()
    capacidad = IntegerField()
    estado = CharField(max_length=1)
    restaurante = IntegerField(index=True)
    numero_mesa = CharField(max_length=5)
    habilitado = BooleanField(default=True)

    class Meta:
        table_name = "mesas"
