from datos.conexion import conectar_db
from peewee import Model, CharField, IntegerField, AutoField, DateField
database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class trabajadores(BaseModel):
    id_trabajador = AutoField()
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
    fecha_nacimiento = DateField()
    nacionalidad = IntegerField(index=True)
    direccion = IntegerField(index=True)
    telefono = CharField(max_length=12)
