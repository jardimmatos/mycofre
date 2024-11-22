import environ
from cryptography.fernet import Fernet

env = environ.Env()

# Gerar Nova Chave de 32 bits
crypt_key_env = env.str("CRYPT_KEY", "^%^(*)")
CRYPT_KEY = crypt_key_env.encode("utf-8")

f = Fernet(CRYPT_KEY)


def criptografar(value):
    # converter string pra bytes
    mensagem_cripto = f.encrypt(value.encode())
    # devolver em string
    return mensagem_cripto.decode()


def descriptografar(token):
    mensagem_descripto = f.decrypt(token.encode())
    # devolver em string
    return mensagem_descripto.decode()
