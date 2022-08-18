from cgitb import text
from email.policy import default
from hashlib import pbkdf2_hmac
from passlib.context import CryptContext

contexto= CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=20000

)

texto= "AbCdEfGhIj"
encriptado = contexto.hash(texto)
print(encriptado)
print(contexto.verify(texto, encriptado))