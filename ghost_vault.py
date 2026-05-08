# [ARQUIVO: ghost_vault.py]
from cryptography.fernet import Fernet

def gerar_chave_mestra():
    chave = Fernet.generate_key()
    with open("nexus_prime.key", "wb") as key_file:
        key_file.write(chave)
    print("✅ Chave Mestra 'nexus_prime.key' gerada com sucesso.")

def carregar_chave():
    return open("nexus_prime.key", "rb").read()

if __name__ == "__main__":
    gerar_chave_mestra() # Execute uma vez para gerar sua chave
