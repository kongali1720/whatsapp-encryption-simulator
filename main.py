from encryption import encrypt_message
from decryption import decrypt_message

def simulate_whatsapp():
    sender = input("Nomor pengirim: ")
    receiver = input("Nomor penerima: ")
    message = input("Isi pesan: ")

    encrypted = encrypt_message(message)

    # Simpan ke file
    with open("messages/encrypted_messages.txt", "ab") as file:
        file.write(f"{sender} => {receiver} : {encrypted.decode()}\n".encode())

    print("\n[✔] Pesan berhasil dienkripsi dan disimpan!\n")

    # Dekripsi untuk simulasi
    print(f"[🔓] Pesan setelah didekripsi: {decrypt_message(encrypted)}")

if __name__ == "__main__":
    simulate_whatsapp()
