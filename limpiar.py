import os

def limpiar_archivo(origen, destino):
    # Lee el archivo en modo binario para eliminar cualquier byte nulo o caracter no ASCII visible
    with open(origen, "rb") as f:
        contenido = f.read()

    # Si venía en UTF-16 con BOM o bytes nulos
    if b"\x00" in contenido:
        # Intentar decodificar como utf-16
        try:
            texto = contenido.decode("utf-16")
        except Exception:
            texto = contenido.replace(b"\x00", b"").decode("utf-8", errors="ignore")
    else:
        try:
            texto = contenido.decode("utf-8")
        except Exception:
            texto = contenido.decode("latin-1", errors="ignore")

    # Limpiar retornos de carro problemáticos y normalizar saltos de línea
    lineas = texto.splitlines()
    texto_limpio = "\n".join(linea.rstrip() for linea in lineas) + "\n"

    # Guardar en UTF-8 estándar
    with open(destino, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto_limpio)

    print(f"¡Listo! Se guardó '{destino}' totalmente limpio.")

# Ejecutar sobre models.py
limpiar_archivo("datos/models.py", "datos/models_limpio.py")