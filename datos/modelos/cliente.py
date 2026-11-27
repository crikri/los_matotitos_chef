from datos.conexion import conectar_db
from peewee import Model, AutoField, CharField, BooleanField
database = conectar_db()


class BaseModel(Model):
    class Meta:
        database = database


class Cliente(BaseModel):
    id_cliente = AutoField()
    rut = CharField(max_length=12, unique=True)
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
    telefono = CharField(max_length=12)
    email = CharField(max_length=50)
    habilitado = BooleanField(default=True)

    class Meta:
        table_name = 'clientes'
