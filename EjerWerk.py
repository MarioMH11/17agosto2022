from hashlib import sha512
from werkzeug.security import generate_password_hash, check_password_hash

texto="AbCdEfGh"
encriptado= generate_password_hash(texto)
print("")
encriptado2=generate_password_hash(texto, 'sha512')
print("")
encriptado3=generate_password_hash(texto,'pbkdf2:sha256:30',30)
print(encriptado)
print(encriptado2)
print(encriptado3)
print(check_password_hash(encriptado,texto))
print(check_password_hash(encriptado2,texto))

