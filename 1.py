def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if mode == "encrypt":
                new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            elif mode == "decrypt":
                new_char = chr(((ord(char.lower()) - 97 - shift_amount) % 26) + 97)
            else:
                raise ValueError("Invalid mode. Choose either 'encrypt' or 'decrypt'.")
            if char.isupper():
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    return result

# Get user input
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
mode = input("Enter the mode (encrypt/decrypt): ")

# Encrypt or decrypt the message
if mode.lower() == "encrypt":
    encrypted_message = caesar_cipher(message, shift, mode)
    print("Encrypted message:", encrypted_message)
elif mode.lower() == "decrypt":
    decrypted_message = caesar_cipher(message, shift, mode)
    print("Decrypted message:", decrypted_message)
else:
    print("Invalid mode. Choose either 'encrypt' or 'decrypt'.")
