from peewee import *
from datos.conexion import conectar_db
database = conectar_db()
defecto = "DEFAULT 1"

class UnknownField(object):
    def __init__(self, *args, **kwargs): pass


class Comunas(BaseModel):
    codigo_comuna = CharField(max_length=5)
    comuna = CharField(max_length=30)
    id_comuna = AutoField()

    class Meta:
        table_name = 'comunas'

class Direcciones(BaseModel):
    calle = CharField(max_length=50)
    comuna = IntegerField(index=True)
    departamento = CharField(max_length=10, null=True)
    id_direccion = AutoField()
    numero = CharField(max_length=10)

    class Meta:
        table_name = 'direcciones'

class EstadoReserva(BaseModel):
    estado = CharField(max_length=20)
    id_estado = AutoField()

    class Meta:
        table_name = 'estado_reserva'

class Horarios(BaseModel):
    dia_semana = CharField(max_length=10)
    hora_inicio = TimeField()
    hora_termino = TimeField()
    id_horario = AutoField()

    class Meta:
        table_name = 'horarios'

class Paises(BaseModel):
    id_pais = AutoField()
    iso_2 = CharField(max_length=2, null=True)
    iso_3 = CharField(max_length=3, null=True)
    nacionalidad = CharField(max_length=30)
    nombre = CharField(max_length=60)

    class Meta:
        table_name = 'paises'

class Reservas(BaseModel):
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

class RestauranteMesas(BaseModel):
    id_restaurante_mesa = AutoField()
    mesa = IntegerField(index=True)
    restaurante = IntegerField(index=True)

    class Meta:
        table_name = 'restaurante_mesas'

class Restaurantes(BaseModel):
    direccion = IntegerField(index=True)
    email = CharField(max_length=50)
    id_restaurantes = AutoField()
    nombre = CharField(max_length=50)
    telefono = CharField(max_length=12)
    website = CharField(max_length=50, null=True)

    class Meta:
        table_name = 'restaurantes'

class RestaurantesHorarios(BaseModel):
    horario = IntegerField(index=True)
    id_restaurante_horario = AutoField()
    restaurante = IntegerField(index=True)

    class Meta:
        table_name = 'restaurantes_horarios'

class RestaurantesTrabajadores(BaseModel):
    id_restaurante_trabajador = AutoField()
    restaurante = IntegerField(index=True)
    trabajador = IntegerField(index=True)

    class Meta:
        table_name = 'restaurantes_trabajadores'
