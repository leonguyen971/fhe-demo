# decrypt.py

def decrypt(data: str) -> str:
    """Validate format and decrypt"""
    if not data.startswith("<enc>") or not data.endswith("</enc>"):
        raise ValueError("Invalid encrypted data format")
    return data.replace("<enc>", "").replace("</enc>", "")

if __name__ == "__main__":
    encrypted = "<enc>Hello</enc>"
    print("Decrypted:", decrypt(encrypted))
