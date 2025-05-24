# Criptografia AES (CPF, endereço, nascimento)
import zipfile
from cryptography.fernet import Fernet

def generate_and_zip_key():
    key = Fernet.generate_key()
    with zipfile.ZipFile("key.zip", "w") as zipf:
        zipf.writestr("secret.key", key)

def load_key_from_zip():
    with zipfile.ZipFile("key.zip", "r") as zipf:
        return zipf.read("secret.key")

def get_fernet():
    key = load_key_from_zip()
    return Fernet(key)

def encrypt_data(data: str) -> str:
    fernet = get_fernet()
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(data: str) -> str:
    fernet = get_fernet()
    return fernet.decrypt(data.encode()).decode()
