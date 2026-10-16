from datos.conexion import conectar_db
from peewee import Model, AutoField, IntegerField, DateField, TimeField
database = conectar_db()


class BaseModel(Model):
    class Meta:
        database = database


class Reserva(BaseModel):
    cantidad_personas = IntegerField()
    cliente = IntegerField(index=True)
    estado = IntegerField(index=True)
    fecha = DateField()
    hora_inicio = TimeField()
    hora_termino = TimeField()
    id_reserva = AutoField()
    mesa = IntegerField(index=True)

    class Meta:
        table_name = 'reservas'