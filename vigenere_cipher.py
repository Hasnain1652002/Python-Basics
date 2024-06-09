import string
import pandas as pd 
from itertools import cycle

# constants
# VIGENERE_TABLE = {
#     letter: {
#         char: string.ascii_uppercase[
#             (string.ascii_uppercase.index(letter) + string.ascii_uppercase.index(char))
#             % 26
#         ]
#         for char in string.ascii_uppercase
#     }
#     for letter in string.ascii_uppercase
# }


# INVERSE_VIGENERE_TABLE = {
#     letter: {VIGENERE_TABLE[letter][char]: char for char in string.ascii_uppercase}
#     for letter in string.ascii_uppercase
# }

TOTAL_ALPHABETS = 26

# # Using table-based approach
# def vigenere_cipher_table_based(text, keyword, mode="encrypt"):
#     keyword_cycle = cycle(keyword.upper())
#     print(keyword_cycle)
#     result = ""
#     for char in text:
#         if char.upper() in string.ascii_uppercase:
#             table = VIGENERE_TABLE if mode == "encrypt" else INVERSE_VIGENERE_TABLE
#             result += (
#                 table[next(keyword_cycle)][char.upper()]
#                 if char.isupper()
#                 else table[next(keyword_cycle)][char.upper()].lower()
#             )
#         else:
#             result += char

#     return result


# Using math-based or formula-based approach
def vigenere_cipher_math_based(message, keyword, mode="encrypt"):
    result = ""
    keyword_cycle = cycle(keyword.upper())
    for char in message:
        if char.upper() in string.ascii_uppercase:
            # print(string.ascii_uppercase.index(next(keyword_cycle)))
            shift = string.ascii_uppercase.index(next(keyword_cycle))
            if mode == "decrypt":
                shift = -shift
            # print(shift)
            result += (
                string.ascii_uppercase[
                    (string.ascii_uppercase.index(char) + shift) % TOTAL_ALPHABETS
                ]
                if char.isupper()
                else string.ascii_lowercase[
                    (string.ascii_lowercase.index(char) + shift) % TOTAL_ALPHABETS
                ]
            )
        else:
            result += char

    return result


if __name__ == "__main__":
    # print(pd.DataFrame(VIGENERE_TABLE))
    # print(pd.DataFrame(INVERSE_VIGENERE_TABLE))

    plaintext = input(" Enter your message: ")
    key = input(" Enter the key: ")
    cipher_text = vigenere_cipher_math_based(plaintext, key)

    print("\n Encryption using Vigenere Cipher Math-based Approach:")
    print(f"    Plaintext: {plaintext}")
    print(f"    Key: {key}")
    print(f"    Ciphertext: {cipher_text}")

    ask_to_decrypt = input("\n Do you want to decrypt the message? (Y/N): ").lower()
    if ask_to_decrypt == "y":
        decrypted_text = vigenere_cipher_math_based(cipher_text, key, mode="decrypt")
        print("\n Decryption using Vigenere Cipher Math-based Approach:")
        print(f"    Ciphertext: {cipher_text}")
        print(f"    Key: {key}")
        print(f"    Decrypted text: {decrypted_text}")
