from datos.conexion import conectar_db
from peewee import Model, CharField, AutoField, TimeField
database = conectar_db()


class BaseModel(Model):
    class Meta:
        database = database


class Horario(BaseModel):
    dia_semana = CharField(max_length=10)
    hora_inicio = TimeField()
    hora_termino = TimeField()
    id_horario = AutoField()

    class Meta:
        table_name = 'horarios'