import zlib

# Comprimir datos usando zlib
datos = b'Ejemplo de datos para comprimir.'
datos_comprimidos = zlib.compress(datos)
print("Datos comprimidos:", datos_comprimidos)

# Descomprimir datos
datos_descomprimidos = zlib.decompress(datos_comprimidos)
print("Datos descomprimidos:", datos_descomprimidos)
