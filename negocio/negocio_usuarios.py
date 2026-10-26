import bcrypt
from datetime import date
from prettytable import PrettyTable
from datos.repositorio.repositorio_usuarios import listado_usuarios_habilitados, guardar_usuario
from datos.modelos.usuario import Usuario

def cargar_usuarios(tabla: PrettyTable):
    usuarios = listado_usuarios_habilitados()
    tabla.field_names = ['Id', 'RUT', 'Nombre Completo', 'Email', 'País', 'Fecha Nacimiento', 'Género', 'Fecha Incorporación']

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
                usuario.email, # <-- Cambiado a email
                usuario.pais,
                usuario.fecha_nacimiento,
                genero_usuario,
                usuario.fecha_incorporacion
            ])

    return tabla

def registrar_nuevo_usuario(rut, nombre, apellido, email, pais, fecha_nacimiento, genero, password_plana):
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password_plana.encode('utf-8'), salt).decode('utf-8')

    datos = {
        'rut': rut,
        'nombre': nombre,
        'apellido': apellido,
        'email': email, # <-- Cambiado a email
        'pais': pais,
        'fecha_nacimiento': fecha_nacimiento if fecha_nacimiento else None,
        'genero': genero,
        'fecha_incorporacion': date.today(),
        'habilitado': True,
        'password': password_hash
    }

    return guardar_usuario(datos)