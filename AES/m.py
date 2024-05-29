from CONSTANTS import *
import sys

def pprintMatrix(matrix):
    for row in matrix:
        for value in row:
            print(value,end=" ")
        print()

def fillMatrixColumnWise(HexaDecimalArray):
    matrix = [[0]*4 for _ in range(4)]
    
    for index in range(len(HexaDecimalArray)):
        row = index % 4
        col = index // 4
        matrix[row][col] = HexaDecimalArray[index]

    return matrix

def ASCIITextToHexaDecimalArray(text):
    hexArray = [format(ord(c), '02x') for c in text]
    return hexArray

def HexaDecimalArrayToASCIIText(hexArray):
    asciiText = ''.join([chr(int(x, 16)) for x in hexArray])
    return asciiText

def byteSubstitutionArray(array):
    for i in range(4):
        hexValue = array[i]
        row = int(hexValue[0], 16)
        col = int(hexValue[1], 16)
        array[i] = S_BOX[row * 16 + col]
    return array

def xorTwoArrays(arrayNo1, arrayNo2):
    result = ['{:02x}'.format(int(a, 16) ^ int(b, 16)) for a, b in zip(arrayNo1, arrayNo2)]
    return result

def convertFrom2DTo1D(array):
    result = [element for i in array for element in i]
    return result

def stateMatrixToHexList(stateMatrix):
    result = []
    for i in range(4):
        for j in range(4):
            result.append(stateMatrix[j][i]) 
    return result

def generateRoundKey(hexValue, roundNumber):
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
    roundKeys = []
    roundKey = ASCIITextToHexaDecimalArray(key)    
    roundKeys.append(roundKey)
    
    for i in range (10):
        roundKey = generateRoundKey(roundKey, i)
        roundKeys.append(roundKey)

    return roundKeys

def circularLeftShift(array, positions):
    positions = positions % len(array)  
    return array[positions:] + array[:positions]

def substitueBytes(stateMatrix):
    for i in range(4):
        for j in range(4):
            hexValue = stateMatrix[i][j]
            row = int(hexValue[0], 16)
            col = int(hexValue[1], 16)
            stateMatrix[i][j] = S_BOX[row * 16 + col]
    return stateMatrix

def shiftRows(stateMatrix):
    for i in range(1, 4):
        stateMatrix[i] = circularLeftShift(stateMatrix[i], i)
    return stateMatrix

def multiplyGF(x, y):
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
    for i in range(4):
        stateMatrix1[i] = xorTwoArrays(stateMatrix1[i], stateMatrix2[i])
    return stateMatrix1

def circularRightShift(array, positions):
    positions = positions % len(array)
    return array[len(array)-positions:] + array[:len(array)-positions]

def inverseSubstitueBytes(stateMatrix):
    for i in range(4):
        for j in range(4):
            hexValue = stateMatrix[i][j]
            row = int(hexValue[0], 16)
            col = int(hexValue[1], 16)
            stateMatrix[i][j] = INVERSE_S_BOX[row * 16 + col]
    return stateMatrix

def inverseShiftRows(stateMatrix):
    for i in range(1, 4):
        stateMatrix[i] = circularRightShift(stateMatrix[i], i)
    return stateMatrix

def inverseMixColumns(stateMatrix):
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
    keyStateMatrix = fillMatrixColumnWise(roundKeys[0])
    stateMatrix      = addRoundKey(keyStateMatrix, plaintextStateMatrix)

    for i in range(9):
        keyStateMatrix   = fillMatrixColumnWise(roundKeys[i+1])
        stateMatrix      = substitueBytes(stateMatrix)
        stateMatrix      = shiftRows(stateMatrix)
        stateMatrix      = mixColumns(stateMatrix)
        stateMatrix      = addRoundKey(keyStateMatrix, stateMatrix)

    keyStateMatrix   = fillMatrixColumnWise(roundKeys[10])
    stateMatrix      = substitueBytes(stateMatrix)
    stateMatrix      = shiftRows(stateMatrix)
    stateMatrix      = addRoundKey(keyStateMatrix, stateMatrix)

    cipherText = stateMatrixToHexList(stateMatrix)
    cipherText = HexaDecimalArrayToASCIIText(cipherText)

    return cipherText

def decryption(cipherStateMatrix, roundKeys):
    keyStateMatrix = fillMatrixColumnWise(roundKeys[10])
    decryptMatrix  = addRoundKey(keyStateMatrix, cipherStateMatrix)

    for count,i in enumerate(range(9, 0, -1),start=1):
        keyStateMatrix1 = fillMatrixColumnWise(roundKeys[i])
        decryptMatrix   = inverseShiftRows(decryptMatrix)
        decryptMatrix   = inverseSubstitueBytes(decryptMatrix)
        decryptMatrix   = addRoundKey(keyStateMatrix1, decryptMatrix)
        decryptMatrix   = inverseMixColumns(decryptMatrix)

    keyStateMatrix1 = fillMatrixColumnWise(roundKeys[0])
    decryptMatrix   = inverseShiftRows(decryptMatrix)
    decryptMatrix   = inverseSubstitueBytes(decryptMatrix)
    decryptMatrix   = addRoundKey(keyStateMatrix1, decryptMatrix)

    decryptedText = stateMatrixToHexList(decryptMatrix)
    decryptedText = HexaDecimalArrayToASCIIText(decryptedText)

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

    plainTextHexMatrix = fillMatrixColumnWise(plainTextHex)
    keyHexMatrix       = fillMatrixColumnWise(keyHex)
    
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

    cipherTextHexMatrix = fillMatrixColumnWise(cipherTextHex)
    keyHexMatrix        = fillMatrixColumnWise(keyHex)

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
