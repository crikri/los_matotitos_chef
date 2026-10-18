from datos.repositorio.respositorio_restaurantes import (
    listado_restaurantes,
    insertar_restaurante,
    restaurante_por_id,
    guardar_restaurante
)


def cargar_restaurantes(tabla_restaurantes):
    restaurantes = listado_restaurantes()
    tabla_restaurantes.field_names = [
        "ID", "Nombre", "Dirección", "Teléfono", "Email", "Sitio Web"
    ]
    tabla_restaurantes.align["Nombre"] = "l"
    tabla_restaurantes.align["Email"] = "l"

    for r in restaurantes:
        web = r.website if r.website else "N/A"
        tabla_restaurantes.add_row([
            r.id_restaurantes,
            r.nombre,
            r.direccion,
            r.telefono,
            r.email,
            web
        ])
    return tabla_restaurantes


def registrar_nuevo_restaurante(nombre, direccion, email, telefono, website=None):
    if not nombre or not nombre.strip():
        print("El nombre no puede estar vacío.")
        return False

    if not str(direccion).strip().isdigit():
        print("La dirección debe ser un número entero.")
        return False

    if not email or not email.strip():
        print("El email no puede estar vacío.")
        return False

    if not telefono or not telefono.strip():
        print("El teléfono no puede estar vacío.")
        return False

    website_limpio = website.strip() if website and website.strip() else None

    resultado = insertar_restaurante(
        nombre=nombre.strip(),
        direccion=int(direccion),
        email=email.strip(),
        telefono=telefono.strip(),
        website=website_limpio
    )
    return resultado is not None


def eliminar_restaurante_logico(id_rest):
    if not str(id_rest).strip().isdigit():
        print("El ID debe ser un número entero.")
        return False

    restaurante = restaurante_por_id(id_rest)
    if not restaurante:
        print(f"No se encontró el restaurante con ID {id_rest}.")
        return False

    if not restaurante.habilitado:
        print("El restaurante ya se encuentra deshabilitado.")
        return False

    restaurante.habilitado = False
    resultado = guardar_restaurante(restaurante)
    return resultado is not None
