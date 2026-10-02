from datos.conexion import conectar_db
from peewee import Model

database = conectar_db()
def modelo_inicial():
    class BaseModel(Model):
        class Meta:
            database = database
            self.