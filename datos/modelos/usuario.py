from datos.conexion import conectar_db
from peewee import Model, AutoField, CharField, IntegerField, DateField, BooleanField, ForeignKeyField
from datos.modelos.pais import Pais

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Usuario(BaseModel):
    id_usuario = AutoField()
    rut = CharField(max_length=12)
    nombre = CharField(max_length=25, null=False)
    apellido = CharField(max_length=25, null=False)
    email = CharField(max_length=255, null=False)
    # En la BD se guarda el id (columna 'pais'); usuario.pais entrega el objeto Pais
    # y usuario.pais_id entrega el id.
    pais = ForeignKeyField(Pais, column_name='pais', field='id_pais',
                           backref='usuarios', null=True)
    fecha_nacimiento = DateField(null=True)
    genero = IntegerField(null=False)
    fecha_incorporacion = DateField(null=False)
    habilitado = BooleanField(default=True)
    password = CharField(max_length=60, null=True)

    class Meta:
        table_name = 'usuarios'