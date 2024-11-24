def caesar_cipher_encrypt(text, shift):
    """Encrypts text using Caesar cipher."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    """Decrypts text using Caesar cipher."""
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    while True:
        choice = input("Choose an option: (1) Encrypt (2) Decrypt (3) Exit: ").strip()
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
