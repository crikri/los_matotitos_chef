from datos.conexion import conectar_db
from peewee import Model, CharField, IntegerField, AutoField, DateField
database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Restaurante_trabajador(BaseModel):
    id_restaurante_trabajadores = AutoField()
    restaurante = IntegerField(index=True)
    trabajador = IntegerField(index=True)
    
    class Meta:
        table_name = "restaurante_trabajadores"
