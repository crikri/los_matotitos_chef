from datos.conexion import conectar_db
from peewee import Model, CharField, AutoField
database = conectar_db()


class BaseModel(Model):
    class Meta:
        database = database


class EstadoReserva(BaseModel):
    estado = CharField(max_length=20)
    id_estado = AutoField()

    class Meta:
        table_name = 'estado_reserva'