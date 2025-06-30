from encrypt import encrypt
from decrypt import decrypt

if __name__ == "__main__":
    data = "secret"
    encrypted = encrypt(data)
    print("Encrypted:", encrypted)

    decrypted = decrypt(encrypted)
    print("Decrypted:", decrypted)
