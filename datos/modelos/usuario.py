from datos.conexion import conectar_db
from datos.modelos.direccion import Direccion
from peewee import Model, CharField, IntegerField, AutoField, DateField, BooleanField
database = conectar_db()


class BaseModel(Model):
    class Meta:
        database = database


class Usuario(BaseModel):
    id_usuario = AutoField()
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
    direccion = IntegerField(index=True),
    rut = CharField(max_length=12, unique=True)
    email = CharField(max_length=50)
    fecha_nacimiento = DateField()
    nacionalidad = IntegerField(index=True)
    telefono = CharField(max_length=12),
    habilitado = BooleanField(default=True),
    contrasena = CharField(max_length=60, null=True)

    class Meta:
        table_name = "usuarios"