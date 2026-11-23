import bcrypt
from datetime import date
from prettytable import PrettyTable
from datos.repositorio.repositorio_usuarios import listado_usuarios_habilitados, guardar_usuario
from datos.modelos.usuario import Usuario
from datetime import datetime


def cargar_usuarios(tabla: PrettyTable):
    usuarios = listado_usuarios_habilitados()
    tabla.field_names = ['Id', 'RUT', 'Nombre Completo', 'Email',
                         'País', 'Fecha Nacimiento', 'Género', 'Fecha Incorporación']

    if usuarios:
        for usuario in usuarios:
            nombre_completo = f"{usuario.nombre} {usuario.apellido}"
            genero_usuario = ''
            match usuario.genero:
                case 184:
                    genero_usuario = 'Masculino'
                case 185:
                    genero_usuario = 'Femenino'
                case 186:
                    genero_usuario = 'Otro'

            tabla.add_row([
                usuario.id_usuario,
                usuario.rut,
                nombre_completo,
                usuario.email,
                usuario.pais.nombre if usuario.pais else 'Sin país',
                usuario.fecha_nacimiento,
                genero_usuario,
                usuario.fecha_incorporacion
            ])

    return tabla


def registrar_nuevo_usuario(rut, nombre, apellido, email, pais, fecha_nacimiento, genero, password_plana):
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(
        password_plana.encode('utf-8'), salt).decode('utf-8')

    # Convertimos la opción [1-3] al ID real en la base de datos
    id_genero = None
    match genero:
        case '1':
            id_genero = 184
        case '2':
            id_genero = 185
        case '3':
            id_genero = 186

    datos = {
        'rut': rut,
        'nombre': nombre,
        'apellido': apellido,
        'email': email,
        'pais': pais,
        'fecha_nacimiento': fecha_nacimiento if fecha_nacimiento else None,
        'genero': id_genero,  # <--- Usamos el ID convertido (184, 185 o 186)
        'fecha_incorporacion': date.today(),
        'habilitado': True,
        'password': password_hash
    }

    return guardar_usuario(datos)


def modificar_usuario(str_rut, str_nombre, str_apellido, str_correo, id_pais, str_fecha_nacimiento, genero, usuario: Usuario):
    if str_rut != '' and str_rut != usuario.rut:
        usuario.rut = str_rut

    if str_nombre != '' and str_nombre != usuario.nombre:
        usuario.nombre = str_nombre

    if str_apellido != '' and str_apellido != usuario.apellido:
        usuario.apellido = str_apellido

    if str_correo != '' and str_correo != usuario.email:
        usuario.email = str_correo

    # Corrección extra: id_pais viene como string desde input(), conviértelo a int si no está vacío
    # usa usuario.pais si no es ForeignKey
    if id_pais != '' and int(id_pais) != usuario.pais_id:
        usuario.pais = int(id_pais)

    if str_fecha_nacimiento != '' and str_fecha_nacimiento != usuario.fecha_nacimiento:
        usuario.fecha_nacimiento = datetime.strptime(
            str_fecha_nacimiento, "%d/%m/%Y")

    if genero != '' and genero != usuario.genero:
        match genero:
            case '1':
                usuario.genero = 184
            case '2':
                usuario.genero = 185
            case '3':
                usuario.genero = 186

    # Guardamos los cambios directamente con .save() en lugar de llamar a guardar_usuario()
    try:
        usuario.save()
        print('Usuario actualizado con éxito')
    except Exception as e:
        print(f"Error en la base de datos al actualizar usuario: {e}")
