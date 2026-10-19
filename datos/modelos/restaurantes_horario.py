from datos.conexion import conectar_db
from peewee import Model, CharField, IntegerField, AutoField, DateField
database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Restaurante_horario(BaseModel):
    id_restaurante_horarios = AutoField()
    restaurante = IntegerField(index=True)
    horario = IntegerField(index=True)

    class Meta:
        table_name = "restaurante_horarios"
        