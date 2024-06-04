def prepare_key(key):
    key = key.upper().replace(" ", "")
    key = key.replace("J", "I")
    key = "".join(sorted(set(key), key=key.index))
    return key

def generate_key_matrix(key):
    key = prepare_key(key)
    key_matrix = []
    for char in key:
        if char not in key_matrix and char != "J":
            key_matrix.append(char)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in key_matrix:
            key_matrix.append(char)
    key_matrix = [key_matrix[i:i+5] for i in range(0, 25, 5)]
    return key_matrix

def find_char_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def encrypt(message, key):
    key_matrix = generate_key_matrix(key)
    message = message.upper().replace(" ", "")
    message = message.replace("J", "I")
    for i in range(1, len(message)):
        if message[i] == message[i-1]:
            message = message[:i] + "X" + message[i:]
    if len(message) % 2 != 0:
        message += "X"
    encrypted_message = ""
    for i in range(0, len(message), 2):
        char1, char2 = message[i], message[i+1]
        row1, col1 = find_char_position(key_matrix, char1)
        row2, col2 = find_char_position(key_matrix, char2)
        if row1 == row2:
            encrypted_message += key_matrix[row1][(col1 + 1) % 5]
            encrypted_message += key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_message += key_matrix[(row1 + 1) % 5][col1]
            encrypted_message += key_matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_message += key_matrix[row1][col2]
            encrypted_message += key_matrix[row2][col1]
    return encrypted_message

def decrypt(encrypted_message, key):
    key_matrix = generate_key_matrix(key)
    decrypted_message = ""
    for i in range(0, len(encrypted_message), 2):
        char1, char2 = encrypted_message[i], encrypted_message[i+1]
        row1, col1 = find_char_position(key_matrix, char1)
        row2, col2 = find_char_position(key_matrix, char2)
        if row1 == row2:
            decrypted_message += key_matrix[row1][(col1 - 1) % 5]
            decrypted_message += key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_message += key_matrix[(row1 - 1) % 5][col1]
            decrypted_message += key_matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_message += key_matrix[row1][col2]
            decrypted_message += key_matrix[row2][col1]
    return decrypted_message

# Example usage:
key = "SECURiTY"
message = "KILL"
encrypted_message = encrypt(message, key)
print("Encrypted Cipher Text : ",'\n', encrypted_message)
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted Message Text : ",'\n', decrypted_message)
