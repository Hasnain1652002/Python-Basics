def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha(): 
            shifted = ord(char) + shift % 26
            # if char.islower():
            #     if shifted > ord('z'):
            #         shifted -= 26
            # elif char.isupper():
            #     if shifted > ord('Z'):
            #         shifted -= 26
            encrypted_text += chr(shifted)
        elif char.isdigit():
            shifted = ord(char) + shift
            encrypted_text += chr(shifted)
        else:
            shifted = ord(char) + shift
            encrypted_text += chr(shifted)

    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha(): 
            shifted = ord(char) - shift % 26
            # if char.islower():
            #     if shifted < ord('a'):
            #         shifted += 26
            # elif char.isupper():
            #     if shifted < ord('A'):
            #         shifted += 26
            decrypted_text += chr(shifted)
        elif char.isdigit():
            shifted = ord(char) - shift
            decrypted_text += chr(shifted)
        else:
            shifted = ord(char) - shift
            decrypted_text += chr(shifted)
            
    return decrypted_text


plaintext = input("Enter Message : ")
shift = int(input("Enter a Key : "))

print("                 Encryption")
encrypted_text = caesar_encrypt(plaintext, shift)
print("Message:", plaintext)
print("Encrypted:", encrypted_text)
print("\n\n                 Decryption")
decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Encrypted Message:", encrypted_text)
print("Decrypted:", decrypted_text)
