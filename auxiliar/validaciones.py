import re

def validar_rut(rut):
    """
    Valida un RUT chileno.

    Args:
        rut (str): El RUT a validar, en formato "XXXXXXXX-X" o "XXXXXXXXX".

    Returns:
        bool: True si el RUT es válido, False en caso contrario.
    """
    # Eliminar puntos y guiones
    rut = rut.replace(".", "").replace("-", "")

    # Verificar que el RUT tenga al menos 2 caracteres
    if len(rut) < 2:
        return False

    # Separar el dígito verificador del resto del RUT
    cuerpo = rut[:-1]
    dv = rut[-1].upper()

    # Calcular el dígito verificador esperado
    suma = 0
    multiplicador = 2

    for digito in reversed(cuerpo):
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    resto = suma % 11
    dv_calculado = 11 - resto

    if dv_calculado == 11:
        dv_calculado = '0'
    elif dv_calculado == 10:
        dv_calculado = 'K'
    else:
        dv_calculado = str(dv_calculado)

    return dv == dv_calculado

def validar_correo(correo):
    patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(patron_correo, correo):
        print('Correo electrónico NO corresponde, ingrese nuevamente...')
        correo = ''
    return correo

def validar_contrasenia(contrasenia):
    patron_contrasenia = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){8,15}$'
    if not re.match(patron_contrasenia, contrasenia):
        print('Su contraseña NO es segura, ingrese nuevamente...')
        contrasenia = ''
    return contrasenia