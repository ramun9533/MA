# Codificación binaria de un mensaje
mensaje = "Hola Mundo"
mensaje_codificado = ''.join(format(ord(caracter), '08b') for caracter in mensaje)
print("Mensaje codificado:", mensaje_codificado)
