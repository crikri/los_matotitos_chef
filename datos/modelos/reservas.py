from datos.conexion import conectar_db
from peewee import Model, CharField, IntegerField, AutoField, DateField
database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class reservas(BaseModel):
    id_reserva = AutoField()
    cliente = IntegerField(index=True)
    estado_reserva = IntegerField(index=True)
    fecha_reserva = DateField()
    hora_inicio = TimeField()
    hora_termino = TimeField()
    cantidad_personas = IntegerField()

    class Meta: 
        table_name = "reservas"
        