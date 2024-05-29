from CONSTANTS import *
import sys

def pprintMatrix(matrix):
    for row in matrix:
        for value in row:
            print(value,end=" ")
        print()

def fillMatrixColumnWise(HexaDecimalArray):
    
    """
        * Creating a 4x4 matrix initialized with 
          zeros.
        * Filling the matrix column-wise.
        * Returing the matrix.  
    """
    matrix = [[0]*4 for _ in range(4)]
    
    for index in range(len(HexaDecimalArray)):
        row = index % 4
        col = index // 4
        matrix[row][col] = HexaDecimalArray[index]

    return matrix


def ASCIITextToHexaDecimalArray(text):
    """
        * Converting ascii text to hexa-decimal 
          array.
        * Returning the hex array. 
    """
    hexArray = [format(ord(c), '02x') for c in text]
    return hexArray

def HexaDecimalArrayToASCIIText(hexArray):
    """
      * Converting hex array to ascii text.
      * Returning ascii text
    """
    asciiText = ''.join([chr(int(x, 16)) for x in hexArray])
    return asciiText

def byteSubstitutionArray(array):
    """
        * Performing byte substitution using an S-box.
        * Getting the hexadecimal string value, converting first digit
          to decimal for row index, converting second digit to decimal 
          for column index and using the combined index to lookup 
          the S-box.
        * Returning the resultant array.
    """
    for i in range(4):
        hexValue = array[i]
        row = int(hexValue[0], 16)
        col = int(hexValue[1], 16)
        array[i] = S_BOX[row * 16 + col]
    return array

def xorTwoArrays(arrayNo1, arrayNo2):
    """
        * Performing XOR operation and formatting results to 
          hexadecimal strings.
        * Returning the result.
    """
    result = ['{:02x}'.format(int(a, 16) ^ int(b, 16)) for a, b in zip(arrayNo1, arrayNo2)]
    return result

def convertFrom2DTo1D(array):
    """
        * Flattenning the 2D array using a list comprehension.
        * Returning the result.
    """
    result = [element for i in array for element in i]
    return result

def stateMatrixToHexList(stateMatrix):
    """
        * Transforming a state matrix into a 1D list by 
          iterating through each column and appending 
          elements row by row. This structure ensures 
          proper conversion and maintains consistency.
        * Returning the result.
    """
    result = []
    for i in range(4):
        for j in range(4):
            result.append(stateMatrix[j][i]) 
    return result

def generateRoundKey(hexValue, roundNumber):
    """
        * Generating a round key.
        * Initializes a state matrix using the hexadecimal values.
        * Performs a 1-byte circular left shift on the fourth row (w[3]).
        * Substitutes each byte in w[3] using an S-box.
        * Applies a round constant to w[3] using an XOR operation.
        * Computes subsequent rows w[4], w[5], w[6], and w[7] iteratively 
          using XOR operations.
        * Converts the state matrix into a 1D list and returns it as 
          the round key.
        * Returning round key.
    """
    stageMatrix = fillMatrixColumnWise(hexValue)
    gMatrix     = circularLeftShift(stageMatrix[3], 1)
    gMatrix     = byteSubstitutionArray(gMatrix)
    gMatrix     = xorTwoArrays(gMatrix, RCON[roundNumber])

    stageMatrix[0] = xorTwoArrays(stageMatrix[0], gMatrix)

    j = 0
    for i in range(3):
        stageMatrix[j+1] = xorTwoArrays(stageMatrix[j], stageMatrix[j+1])
        j += 1

    roundKey = convertFrom2DTo1D(stageMatrix)
    return roundKey

def keyExpansion(key):
    """
        * Generating 11 round keys from a single initial key .
        * Converting the initial key from ASCII to hexadecimal.
        * Adding the converted key as the first round key.
        * Iteratively generating 10 more round keys using the 
          `generateRoundKey` function, and appends them to 
          the list.
        * Returning a list of 11 lists, each containing 16 
          hexadecimal strings,representing the round keys.
    """
    roundKeys = []
    roundKey = ASCIITextToHexaDecimalArray(key)    
    roundKeys.append(roundKey)
    
    for i in range (10):
        roundKey = generateRoundKey(roundKey, i)
        roundKeys.append(roundKey)

    return roundKeys



def circularLeftShift(array, positions):
    """    
      * Performing a left rotation on an array by n positions,
        ensuring n is within a valid range. 
      * Returning a new array by splitting the input array and
        reordering its parts.
    """
    positions = positions % len(array)  
    return array[positions:] + array[:positions]


def substitueBytes(stateMatrix):
    """
        ################################
        # AES ROUND TRANSFORMATION # 1 #
        ################################

        * Performing a byte substitution on each element of a 4x4 state matrix. 
        * Returning the state matrix with each element replaced by its corresponding
          S-box value.
    """
    for i in range(4):
        for j in range(4):
            hexValue = stateMatrix[i][j]
            row = int(hexValue[0], 16)
            col = int(hexValue[1], 16)
            stateMatrix[i][j] = S_BOX[row * 16 + col]
    return stateMatrix


def shiftRows(stateMatrix):
    """
     ################################
     # AES ROUND TRANSFORMATION # 2 #
     ################################

     * Performing a row shift on the state matrix.
     * Returning the state matrix with each row i shifted left by i positions.
    """
    for i in range(1, 4):
        stateMatrix[i] = circularLeftShift(stateMatrix[i], i)
    return stateMatrix


def multiplyGF(x, y):
    """
        * Multiplying two integers in GF(2^8), performing bitwise operations.
        * Returning the product of x and y in GF(2^8).
    """
    result = 0
    while y:
        if y & 1:
            result ^= x
        if x & 0x80:
            x = (x << 1) ^ 0x11b
        else:
            x <<= 1
        y >>= 1
    return result


def mixColumns(stateMatrix):
    """
        ################################
        # AES ROUND TRANSFORMATION # 3 #
        ################################

        * Mixes the columns of a state matrix using GF(2^8) multiplication.
        * Returning the state matrix with each column mixed, converting 
          integers back to hex.
    """
    stateMatrix = [[int(x, 16) for x in row] for row in stateMatrix]

    mixedState = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            mixedState[i][j] = (
                multiplyGF(stateMatrix[0][j], MIX_COLUMNS_MATRIX[i][0]) ^
                multiplyGF(stateMatrix[1][j], MIX_COLUMNS_MATRIX[i][1]) ^
                multiplyGF(stateMatrix[2][j], MIX_COLUMNS_MATRIX[i][2]) ^
                multiplyGF(stateMatrix[3][j], MIX_COLUMNS_MATRIX[i][3])
            )

    mixedStateHex = [['{:02x}'.format(x) for x in row] for row in mixedState]
    return mixedStateHex

def addRoundKey(stateMatrix1, stateMatrix2):
    """
        ################################
        # AES ROUND TRANSFORMATION # 4 #
        ################################

      * XORing each row of two state matrices, producing a new state matrix.
      * Returning a 4x4 matrix of hexadecimal strings, where each row is the
        result of XORing the corresponding rows of stateMatrix1 and 
        stateMatrix2.
    """
    for i in range(4):
        stateMatrix1[i] = xorTwoArrays(stateMatrix1[i], stateMatrix2[i])
    return stateMatrix1

def circularRightShift(array, positions):
    """
    
      * Performing a right rotation on an array by n positions,
        ensuring n is within a valid range. 
      * Returning a new array by splitting the input array and
        reordering its parts.
    """
    positions = positions % len(array)
    return array[len(array)-positions:] + array[:len(array)-positions]


def inverseSubstitueBytes(stateMatrix):
    """
        ################################
        # AES ROUND TRANSFORMATION # 1 #
        ################################

        * Performing an inverse byte substitution on each element of a 4x4 state matrix.
        * Returning the state matrix with each element replaced by its corresponding 
          inverse S-box value.
    """
    for i in range(4):
        for j in range(4):
            hexValue = stateMatrix[i][j]
            row = int(hexValue[0], 16)
            col = int(hexValue[1], 16)
            stateMatrix[i][j] = INVERSE_S_BOX[row * 16 + col]
    return stateMatrix



def inverseShiftRows(stateMatrix):
    """
        ################################
        # AES ROUND TRANSFORMATION # 2 #
        ################################
        * Performs an inverse row shift on the state matrix.
        * The state matrix with each row i shifted right by i positions.
    """
    for i in range(1, 4):
        stateMatrix[i] = circularRightShift(stateMatrix[i], i)
    return stateMatrix


def inverseMixColumns(stateMatrix):
    """
        ################################
        # AES ROUND TRANSFORMATION # 3 #
        ################################

        * Appling the inverse MixColumns transformation to a 4x4 matrix.
        * Returning the state matrix with each column transformed using the inverse 
          MixColumns matrix.
    """
    resultMatrix = [['00'] * 4 for _ in range(4)]
    stateMatrix = [[int(x, 16) for x in row] for row in stateMatrix]

    for col in range(4):
        for row in range(4):
            result = 0
            for i in range(4):
                result ^= multiplyGF(stateMatrix[i][col], INVERSE_MIX_COLUMNS_MATRIX[row][i])
            resultMatrix[row][col] = '{:02x}'.format(result)

    return resultMatrix



def encryption(plaintextStateMatrix, roundKeys):
    """
        * Encrypting a plaintext state matrix using a set of round keys, following 
          an AES-like encryption workflow.
        * Round 0:
            a. Initializing the key state matrix with the first round key.
            b. Appling an AddRoundKey operation between the plaintext and key state matrices.
        * Rounds 1-9:
            a. Substituting bytes using an S-box.
            b. Shifting rows by their row number.
            c. Mixing columns using GF(2^8) operations.
            d. Appling an AddRoundKey operation with the corresponding round key.
        * Round 10:
            a. Substitutin bytes using an S-box.
            b. Shifting rows by their row number.
            c. Appling an AddRoundKey operation with the final round key.
        * Conversion:
            a. Converting the resulting state matrix to a hexadecimal list.
            b. Converting the hexadecimal list to an ASCII string.
        * Returning a string representing the encrypted ciphertext.
    """
    keyStateMatrix = fillMatrixColumnWise(roundKeys[0])
    stateMatrix      = addRoundKey(keyStateMatrix, plaintextStateMatrix)

    # print("""
    #      ##############
    #      # Round No 0 #
    #      ############## 
    #       """)
    # print("Round Key # 0:\n")
    # pprintMatrix(keyStateMatrix)
    # print()
    # print("Add Round Key:\n")
    pprintMatrix(stateMatrix)
    print()
    input("Press enter for new round...")

    for i in range(9):
        # print(f"""
        # ##############
        # # Round No {i+1} #
        # ############## 
        # """)
        keyStateMatrix   = fillMatrixColumnWise(roundKeys[i+1])
        # print(f"Round Key # {i+1}:\n")
        # pprintMatrix(keyStateMatrix)
        # print()
        
        stateMatrix      = substitueBytes(stateMatrix)
        # print(f"Transformation # 1: Substitue Bytes")
        # pprintMatrix(stateMatrix)
        # print()
        stateMatrix      = shiftRows(stateMatrix)
        # print(f"Transformation # 2: Shift Rows")
        # pprintMatrix(stateMatrix)
        # print()
        stateMatrix      = mixColumns(stateMatrix)
        # print(f"Transformation # 3: Mix Columns")
        # pprintMatrix(stateMatrix)
        # print()
        stateMatrix      = addRoundKey(keyStateMatrix, stateMatrix)
        # print(f"Transformation # 4: Add Round Key")
        # pprintMatrix(stateMatrix)
        # print()

        # input("Press enter for new round...")

    # print(f"""
    #     ##############
    #     # Round No 10#
    #     ############## 
    #     """)
    
    keyStateMatrix   = fillMatrixColumnWise(roundKeys[10])
    
    # print(f"Round Key # 10:\n")
    # pprintMatrix(keyStateMatrix)
    # print()
    
    stateMatrix      = substitueBytes(stateMatrix)
    # print(f"Transformation # 1: Substitue Bytes")
    # pprintMatrix(stateMatrix)
    # print()
    stateMatrix      = shiftRows(stateMatrix)
    # print(f"Transformation # 2: Shift Rows")
    # pprintMatrix(stateMatrix)
    # print()
    stateMatrix      = addRoundKey(keyStateMatrix, stateMatrix)
    # print(f"Transformation # 3: Add Round Key")
    # pprintMatrix(stateMatrix)
    # print()

    input("Press enter for getting the cipherText...")
    
    cipherText = stateMatrixToHexList(stateMatrix)
    cipherText = HexaDecimalArrayToASCIIText(cipherText)

    return cipherText

def decryption(cipherStateMatrix, roundKeys):
    """
    * Decrypting a cipher state matrix using a set of round keys.
    * Round 0:
        a. Initializing the key state matrix with the final round key.
        b. Appling an AddRoundKey operation between the cipher and key state matrices.
    * Rounds 1-9:
        a. Appling an inverse shift rows operation.
        b. Performing an inverse byte substitution using an inverse S-box.
        c. Appling an AddRoundKey operation with the corresponding round key.
        d. Appling an inverse MixColumns operation to each column.
    * Round 10:
        a. Appling an inverse shift rows operation.
        b. Performing an inverse byte substitution using an inverse S-box.
        c. Appling an AddRoundKey operation with the first round key.
    * Conversion:
        a. Converting the resulting state matrix into a hexadecimal list.
        b. Converting the hexadecimal list into an ASCII string.
    * Returning a string representing the decrypted text.
    """
    
    keyStateMatrix = fillMatrixColumnWise(roundKeys[10])
    decryptMatrix  = addRoundKey(keyStateMatrix, cipherStateMatrix)
    
    # print("""
    #      ##############
    #      # Round No 0 #
    #      ############## 
    #       """)
    # print("Round Key # 10:\n")
    # pprintMatrix(keyStateMatrix)
    # print()
    # print("Add Round Key:\n")
    # pprintMatrix(decryptMatrix)
    # print()
    # input("Press enter for new round...")
    

    for count,i in enumerate(range(9, 0, -1),start=1):
        # print(f"""
        # ##############
        # # Round No {count} #
        # ############## 
        # """)

        keyStateMatrix1 = fillMatrixColumnWise(roundKeys[i])
        # print(f"Round Key # {i}:\n")
        # pprintMatrix(keyStateMatrix)
        # print()
        decryptMatrix   = inverseShiftRows(decryptMatrix)
        # print(f"Transformation # 1: Inverse Substitue Bytes")
        # pprintMatrix(decryptMatrix)
        # print()
        decryptMatrix   = inverseSubstitueBytes(decryptMatrix)
        # print(f"Transformation # 2: Inverse Shift Rows")
        # pprintMatrix(decryptMatrix)
        # print()
        decryptMatrix   = addRoundKey(keyStateMatrix1, decryptMatrix)
        # print(f"Transformation # 3: Inverse Mix Columns")
        # pprintMatrix(decryptMatrix)
        # print()
        decryptMatrix   = inverseMixColumns(decryptMatrix)
        # print(f"Transformation # 4: Add Round Key")
        # pprintMatrix(decryptMatrix)
        # print()
        
        
        

        # input("Press enter for new round...")

    # print(f"""
    #     ##############
    #     # Round No 10#
    #     ############## 
    #     """)
    keyStateMatrix1 = fillMatrixColumnWise(roundKeys[0])
    # print(f"Round Key # 0:\n")
    # pprintMatrix(keyStateMatrix)
    # print()
    decryptMatrix   = inverseShiftRows(decryptMatrix)
    # print(f"Transformation # 1: Inverse Substitue Bytes")
    # pprintMatrix(decryptMatrix)
    # print()
    decryptMatrix   = inverseSubstitueBytes(decryptMatrix)
    # print(f"Transformation # 2: Inverse Shift Rows")
    # pprintMatrix(decryptMatrix)
    # print()
    decryptMatrix   = addRoundKey(keyStateMatrix1, decryptMatrix)
    # print(f"Transformation # 3: Add Round Key")
    # pprintMatrix(decryptMatrix)
    # print()
    

    decryptedText = stateMatrixToHexList(decryptMatrix)
    decryptedText = HexaDecimalArrayToASCIIText(decryptedText)
    input("Press enter for getting the decryptedText...")

    return decryptedText



if "__main__" == __name__:

    plainText = input("Enter 128 bit Message to Encrypt : ")
    key       = input("Enter 128 bit Key                : ")

    if len(plainText) != 16:
        print("Error        : Message Length Error :(")
        print("Explaination : Message Length should be 128 bits(16 characters).")
        sys.exit()
    
    if len(key) != 16:
        print("Error        : Key Length Error :(")
        print("Explaination : Key Length should be 128 bits(16 characters).")
        sys.exit()
    
    print()
    input("Press enter to start encryption...")
    print()
    print(f"""
        ##############
        # ENCRYPTION #
        ############## 
        """)
    print()

    plainTextHex = ASCIITextToHexaDecimalArray(plainText)
    keyHex       = ASCIITextToHexaDecimalArray(key)

    # print(f"Converting ASCII Message to HexaDecimal Array.\nMessage :")
    # print(plainTextHex)
    # print()

    # print(f"Converting ASCII Key to HexaDecimal Array.    \nKey     :")
    # print(keyHex)
    # print()

    plainTextHexMatrix = fillMatrixColumnWise(plainTextHex)
    keyHexMatrix       = fillMatrixColumnWise(keyHex)

    # print(f"Converting HexaDecimal Arrays to Column-Wise Matrices.")
    # print()
    
    print(f"plainTextHexMatrix")
    pprintMatrix(plainTextHexMatrix)
    print()
    
    print(f"keyHexMatrix")
    pprintMatrix(keyHexMatrix)
    print()
    
    input("Press enter to start rounds...")

    roundKeys = keyExpansion(key)
    cipherText = encryption(plainTextHexMatrix,roundKeys)
    
    print(f"CipherText : {cipherText} ")
    input("Press enter to start decryption...")
    print()
    print(f"""
        ##############
        # DECRYPTION #
        ############## 
        """)
    cipherTextHex = ASCIITextToHexaDecimalArray(cipherText)
    keyHex       = ASCIITextToHexaDecimalArray(key)

    # print(f"Converting ASCII Message to HexaDecimal Array.\nMessage :")
    # print(cipherTextHex)
    # print()

    # print(f"Converting ASCII Key to HexaDecimal Array.    \nKey     :")
    # print(keyHex)
    # print()

    cipherTextHexMatrix = fillMatrixColumnWise(cipherTextHex)
    keyHexMatrix        = fillMatrixColumnWise(keyHex)

    # print(f"Converting HexaDecimal Arrays to Column-Wise Matrices.")
    # print()
    
    print(f"cipherTextHexMatrix")
    pprintMatrix(cipherTextHexMatrix)
    print()
    
    print(f"keyHexMatrix")
    pprintMatrix(keyHexMatrix)
    print()

    input("Press enter to start rounds...")
    
    roundKeys  = keyExpansion(key)
    plainText = decryption(cipherTextHexMatrix,roundKeys)
    print(f"decryptedText : {plainText} ")
    
