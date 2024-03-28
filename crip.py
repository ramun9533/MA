from cryptography.fernet import Fernet

# Generar una clave de encriptación
clave = Fernet.generate_key()

# Crear un objeto Fernet con la clave generada
cipher = Fernet(clave)

# Encriptar un mensaje
mensaje = b'Ejemplo de mensaje para encriptar.'
mensaje_encriptado = cipher.encrypt(mensaje)
print("Mensaje encriptado:", mensaje_encriptado)

# Desencriptar el mensaje
mensaje_desencriptado = cipher.decrypt(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)
