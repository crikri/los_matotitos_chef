import re

def sanitizar_codigo(archivo_origen, archivo_destino):
    with open(archivo_origen, 'r', encoding='utf-8', errors='replace') as f:
        codigo = f.read()

    # 1. Quitar la marca de orden de bytes (BOM) si existe
    codigo = codigo.lstrip('\ufeff')

    # 2. Reemplazar espacios invisibles y no rompibles por espacios normales
    codigo = re.sub(r'[\u00a0\u202f\u2007\u3000]', ' ', codigo)

    # 3. Eliminar caracteres de ancho cero
    codigo = re.sub(r'[\u200b\u200c\u200d\u2060\ufeff]', '', codigo)

    # 4. Convertir comillas curvas tipográficas en comillas estándar de código
    codigo = re.sub(r'[“”„«»]', '"', codigo)
    codigo = re.sub(r'[‘’`´]', "'", codigo)

    with open(archivo_destino, 'w', encoding='utf-8') as f:
        f.write(codigo)

    print(f"Listo: Se generó '{archivo_destino}' sin caracteres raros.")

# Ruta exacta donde está tu archivo en la carpeta 'datos':
sanitizar_codigo('datos/models.py', 'datos/models_limpio.py')