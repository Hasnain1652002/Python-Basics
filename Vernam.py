def vernam_encrypt(plain_text, key):
    cipher_text = ''
    for char, key_char in zip(plain_text, key):
        plain_num = ord(char) - ord('A')
        key_num = ord(key_char) - ord('A')
        cipher_num = (plain_num + key_num) % 26
        cipher_char = chr(cipher_num + ord('A'))
        cipher_text += cipher_char
    return cipher_text

def vernam_decrypt(cipher_text, key):
    plain_text = ''
    for char, key_char in zip(cipher_text, key):
        cipher_num = ord(char) - ord('A')
        key_num = ord(key_char) - ord('A')
        plain_num = (cipher_num - key_num) % 26
        plain_char = chr(plain_num + ord('A'))
        plain_text += plain_char
    return plain_text

def main():
    print("Vernam Cipher Encryption and Decryption")
    choice = input("Would you like to encrypt or decrypt a message? (e/d): ").lower()
    
    if choice == 'e':
        plain_text = input("Enter the plain text: ").upper()
        key = input("Enter the key (should be same length as plain text): ").upper()
        if len(plain_text) != len(key):
            print("Error: Key length should be same as plain text length.")
            return
        cipher_text = vernam_encrypt(plain_text, key)
        print("Cipher text:", cipher_text)
    
    elif choice == 'd':
        cipher_text = input("Enter the cipher text: ").upper()
        key = input("Enter the key (should be same length as cipher text): ").upper()
        if len(cipher_text) != len(key):
            print("Error: Key length should be same as cipher text length.")
            return
        plain_text = vernam_decrypt(cipher_text, key)
        print("Plain text:", plain_text)
    
    else:
        print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
