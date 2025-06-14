# keygen.py
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[✔] Kunci enkripsi berhasil dibuat!")

if __name__ == "__main__":
    generate_key()
