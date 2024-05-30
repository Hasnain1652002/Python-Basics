from CONSTANTS import *

def bit2Byte(bitList):
    """Convert bit list into a byte list"""
    return [int("".join(map(str,bitList[i*8:i*8+8])),2) for i in range(len(bitList)//8)]
 
def byte2Bit(byteList):
    """Convert byte list into a bit list"""
    return [(byteList[i//8]>>(7-(i%8)))&0x01 for i in range(8*len(byteList))]
 
def permBitList(inputBitList,permTable):
    """Permute input bit list according to input permutation table"""
    return [inputBitList[e - 1] for e in permTable]
 
def permByteList(inByteList,permTable):
    """Permute input byte list according to input permutation table"""
    outByteList = (len(permTable)>>3)*[0]
    for index,elem in enumerate(permTable):
        i = index%8
        e = (elem-1)%8
        if i>=e:
            outByteList[index>>3] |= \
                (inByteList[(elem-1)>>3]&(128>>e))>>(i-e)
        else:
            outByteList[index>>3] |= \
                (inByteList[(elem-1)>>3]&(128>>e))<<(e-i)
    return outByteList
 
def getIndex(inBitList):
    """Permute bits to properly index the S-boxes"""
    return (inBitList[0]<<5)+(inBitList[1]<<3)+ \
           (inBitList[2]<<2)+(inBitList[3]<<1)+ \
           (inBitList[4]<<0)+(inBitList[5]<<4)
 
def padData(string):
    """Add PKCS5 padding to plaintext"""
    padLength = 8-(len(string)%8)
    return [ord(s) for s in string]+padLength*[padLength]
 
def unpadData(byteList):
    """Remove PKCS5 padding from plaintext"""
    return "".join(chr(e) for e in byteList[:-byteList[-1]])
 
def setKey(keyByteList):
    """Generate all sixteen round subkeys"""
    
    def leftShift(inKeyBitList,round):
        """Perform one (or two) circular left shift(s) on key"""
        LStable = (1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1)
 
        outKeyBitList = 56*[0]
        if LStable[round] == 2:
            outKeyBitList[:26] = inKeyBitList[2:28]
            outKeyBitList[26] = inKeyBitList[0]
            outKeyBitList[27] = inKeyBitList[1]
            outKeyBitList[28:54] = inKeyBitList[30:]
            outKeyBitList[54] = inKeyBitList[28]
            outKeyBitList[55] = inKeyBitList[29]
        else:
            outKeyBitList[:27] = inKeyBitList[1:28]
            outKeyBitList[27] = inKeyBitList[0]
            outKeyBitList[28:55] = inKeyBitList[29:]
            outKeyBitList[55] = inKeyBitList[28]
        return outKeyBitList
 
    permKeyBitList = permBitList(byte2Bit(keyByteList),PC1table)
    for round in range(16):
        auxBitList = leftShift(permKeyBitList,round)
        subKeyList[round] = bit2Byte(permBitList(auxBitList,PC2table))
        permKeyBitList = auxBitList
 
def encryptBlock(inputBlock):
    """Encrypt an 8-byte block with already defined key"""
    inputData = permByteList(inputBlock,IPtable)
    leftPart,rightPart = inputData[:4],inputData[4:]
    for round in range(16):
        expRightPart = permByteList(rightPart,EPtable)
        key = subKeyList[round]
        indexList = byte2Bit([i^j for i,j in zip(key,expRightPart)])
        sBoxOutput = 4*[0]
        for nBox in range(4):
            nBox12 = 12*nBox
            leftIndex = getIndex(indexList[nBox12:nBox12+6])
            rightIndex = getIndex(indexList[nBox12+6:nBox12+12])
            sBoxOutput[nBox] = (sBox[nBox<<1][leftIndex]<<4)+ \
                                sBox[(nBox<<1)+1][rightIndex]
        aux = permByteList(sBoxOutput,PFtable)
        newRightPart = [i^j for i,j in zip(aux,leftPart)]
        leftPart = rightPart
        rightPart = newRightPart
    return permByteList(rightPart+leftPart,FPtable)
 
def decryptBlock(inputBlock):
    """Decrypt an 8-byte block with already defined key"""
    inputData = permByteList(inputBlock,IPtable)
    leftPart,rightPart = inputData[:4],inputData[4:]
    for round in range(16):
        expRightPart = permByteList(rightPart,EPtable)
        key = subKeyList[15-round]
        indexList = byte2Bit([i^j for i,j in zip(key,expRightPart)])
        sBoxOutput = 4*[0]
        for nBox in range(4):
            nBox12 = 12*nBox
            leftIndex = getIndex(indexList[nBox12:nBox12+6])
            rightIndex = getIndex(indexList[nBox12+6:nBox12+12])
            sBoxOutput[nBox] = (sBox[nBox*2][leftIndex]<<4)+ \
                                sBox[nBox*2+1][rightIndex]
        aux = permByteList(sBoxOutput,PFtable)
        newRightPart = [i^j for i,j in zip(aux,leftPart)]
        leftPart = rightPart
        rightPart = newRightPart
    return permByteList(rightPart+leftPart,FPtable)
 
def encrypt(key, inString):
    """Encrypt plaintext with given key"""
    setKey(key)
    inByteList,outByteList = padData(inString),[]
    for i in range(0,len(inByteList),8):
        outByteList += encryptBlock(inByteList[i:i+8])
    return outByteList
 
def decrypt(key, inByteList):
    """Decrypt ciphertext with given key"""
    setKey(key)
    outByteList = []
    for i in range(0,len(inByteList),8):
        outByteList += decryptBlock(inByteList[i:i+8])
    return unpadData(outByteList)

if "__main__" == __name__:

    key           = [0x0f, 0x15, 0x71, 0xc9, 0x47, 0xd9, 0xe8, 0x59]
    plaintext     = input("Enter message to encrypt: ")
    ciphertext    = encrypt(key, plaintext)
    encryptedText = ''.join(chr(byte) for byte in ciphertext)
    decryptedText =  decrypt(key, ciphertext)

    print(f"Encrypted Text: {encryptedText}")
    print(f"Decrypted Text: {decryptedText}")
    