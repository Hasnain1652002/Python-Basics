def encrypt(plaintext, key):
    # key = [int(k) for k in key.split()]
    num_columns = len(key)
    num_rows = -(-len(plaintext) // num_columns)
    plaintext += ' ' * (num_rows * num_columns - len(plaintext))
    columns = [''] * num_columns
    for i, char in enumerate(plaintext):
        columns[i % num_columns] += char
    # print(columns)
    rearranged_columns = [columns[k - 1] for k in key]
    ciphertext = ''.join(rearranged_columns)
    return ciphertext

def decrypt(ciphertext, key):
    # key = [int(k) for k in key.split()]
    num_columns = len(key)
    num_rows = -(-len(ciphertext) // num_columns)
    last_row_length = len(ciphertext) % num_columns
    columns = [''] * num_columns
    column_lengths = [num_rows - 1 if i < last_row_length else num_rows for i in range(num_columns)]
    start = 0
    for i, length in enumerate(column_lengths):
        columns[i] = ciphertext[start:start + length]
        start += length
    
    rearranged_columns = [''] * num_columns
    # print(columns)
    for i, k in enumerate(key):
        rearranged_columns[k - 1] = columns[i]
        # print(rearranged_columns)
    plaintext = ''.join([''.join(column) for column in zip(*rearranged_columns)])
    return plaintext

plaintext = "HAMDARD UNIVERSITY KARACHI"
# key = "4 3 5 1 2"
key = "zebras"
sorted_key = sorted(key)
key = list(map(lambda x:sorted_key.index(x)+1,key))

print(key)

ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_plaintext = decrypt(ciphertext, key)
print("Decrypted plaintext:", decrypted_plaintext)
