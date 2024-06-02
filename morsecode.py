MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', 
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', 
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

def encrypt_morse_code(message):
    encrypted_message = ''
    for char in message.upper():
        if char in MORSE_CODE_DICT:
            encrypted_message += MORSE_CODE_DICT[char] + ' '
        elif char == ' ':
            encrypted_message += '/ '
    return encrypted_message.strip()

def decrypt_morse_code(encrypted_message):
    decrypted_message = ''
    for code in encrypted_message.split(' '):
        if code == '/':
            decrypted_message += ' '
        else:
            for char, morse_code in MORSE_CODE_DICT.items():
                if morse_code == code:
                    decrypted_message += char
    return decrypted_message

# Example usage:
message = "KILL general"
encrypted_message = encrypt_morse_code(message)
print("Encrypted cipher text : ",'\n', encrypted_message)

decrypted_message = decrypt_morse_code(encrypted_message)
print("Decrypted message text:",'\n', decrypted_message)
