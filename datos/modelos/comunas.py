from datos.conexion import conectar_db
from peewee import Model, CharField, IntegerField, AutoField, DateField
database = conectar_db()


class BaseModel(Model):
    class Meta:
        database = database
        
class comunas(BaseModel):
    id_comuna = AutoField()
    codigo_comuna = CharField(max_length=5)
    comuna = CharField(max_length=30)

    class Meta:
        table_name = "comunas"


