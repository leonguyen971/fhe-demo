"print('FHE Demo')" 
# encrypt.py

# This function simulates encryption by adding <enc> and </enc> around the input string
def encrypt(data: str) -> str:
    return f"<enc>{data}</enc>"

# Main entry point of the script
if __name__ == "__main__":
    print(encrypt("Hello, world"))

