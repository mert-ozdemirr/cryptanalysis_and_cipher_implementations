import argparse

def codingDictionary():
    lowerCase = "abcdefghijklmnopqrstuvwxyz"
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = [i for i in range(26)]

    lowerDict = dict(zip(lowerCase, nums))
    upperDict = dict(zip(upperCase, nums))

    reverseLowerDict = {v: k for k, v in lowerDict.items()}
    reverseUpperDict = {v: k for k, v in upperDict.items()}

    return [lowerDict, reverseLowerDict, upperDict, reverseUpperDict]


def encrypt_caesar(plaintext, shift):
    convertionDicts = codingDictionary()
    lowerConvertionDict = convertionDicts[0]
    reversedLowerConvertionDict = convertionDicts[1]
    upperConvertionDict = convertionDicts[2]
    reversedUpperConvertionDict = convertionDicts[3]
    
    rightShiftAmount = 26 - shift

    caesarCiphertext = ""
    for i in plaintext:
        try:
            positionLower = lowerConvertionDict[i]
            shiftedPositionLower = (positionLower + rightShiftAmount) % 26
            caesarCiphertext += reversedLowerConvertionDict[shiftedPositionLower]
        except(KeyError):
            try:
                positionUpper = upperConvertionDict[i]
                shiftedPositionUpper = (positionUpper + rightShiftAmount) % 26
                caesarCiphertext += reversedUpperConvertionDict[shiftedPositionUpper]
            except(KeyError):
                caesarCiphertext += i
    
    return caesarCiphertext


def decrypt_caesar(ciphertext, shift):
    convertionDicts = codingDictionary()
    lowerConvertionDict = convertionDicts[0]
    reversedLowerConvertionDict = convertionDicts[1]
    upperConvertionDict = convertionDicts[2]
    reversedUpperConvertionDict = convertionDicts[3]

    rightShiftAmount = shift

    caesarPlaintext = ""
    for i in ciphertext:
        try:
            positionLower = lowerConvertionDict[i]
            shiftedPositionLower = (positionLower + rightShiftAmount) % 26
            caesarPlaintext += reversedLowerConvertionDict[shiftedPositionLower]
        except(KeyError):
            try:
                positionUpper = upperConvertionDict[i]
                shiftedPositionUpper = (positionUpper + rightShiftAmount) % 26
                caesarPlaintext += reversedUpperConvertionDict[shiftedPositionUpper]
            except(KeyError):
                caesarPlaintext += i
    
    return caesarPlaintext


def encrypt_affine(plaintext, a, b):
    convertionDicts = codingDictionary()
    lowerConvertionDict = convertionDicts[0]
    reversedLowerConvertionDict = convertionDicts[1]
    upperConvertionDict = convertionDicts[2]
    reversedUpperConvertionDict = convertionDicts[3]

    affineCiphertext = ""
    for i in plaintext:
        try:
            positionLower = lowerConvertionDict[i]
            shiftedPositionLower = ((positionLower * a) + b) % 26
            affineCiphertext += reversedLowerConvertionDict[shiftedPositionLower]
        except(KeyError):
            try:
                positionUpper = upperConvertionDict[i]
                shiftedPositionUpper = ((positionUpper * a) + b) % 26
                affineCiphertext += reversedUpperConvertionDict[shiftedPositionUpper]
            except(KeyError):
                affineCiphertext += i
    
    return affineCiphertext


def decrypt_affine(ciphertext, a, b):
    convertionDicts = codingDictionary()
    lowerConvertionDict = convertionDicts[0]
    upperConvertionDict = convertionDicts[2]

    lowerCase = "abcdefghijklmnopqrstuvwxyz"
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    transformedNums = [(((i*a)+b)%26) for i in range(26)]
    reversedLowerTransformedDict = dict(zip(transformedNums, lowerCase))
    reversedUpperTransformedDict = dict(zip(transformedNums, upperCase))
    
    affinePlaintext = ""
    for i in ciphertext:
        try:
            affinePlaintext += reversedLowerTransformedDict[lowerConvertionDict[i]]
        except(KeyError):
            try:
                affinePlaintext += reversedUpperTransformedDict[upperConvertionDict[i]]
            except(KeyError):
                affinePlaintext += i
    
    return affinePlaintext


def encrypt_mono(plaintext, key):
    lowerCase = "abcdefghijklmnopqrstuvwxyz"
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    lowerCaseCipher = key.lower()
    upperCaseCipher = key

    lowerTransformedDict = dict(zip(lowerCase, lowerCaseCipher))
    upperTransformedDict = dict(zip(upperCase, upperCaseCipher))

    monoCiphertext = ""
    for i in plaintext:
        try:
            monoCiphertext += lowerTransformedDict[i]
        except(KeyError):
            try:
                monoCiphertext += upperTransformedDict[i]
            except(KeyError):
                monoCiphertext += i
    
    return monoCiphertext


def decrypt_mono(ciphertext, key):
    lowerCase = "abcdefghijklmnopqrstuvwxyz"
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    lowerCaseCipher = key.lower()
    upperCaseCipher = key

    lowerTransformedDict = dict(zip(lowerCaseCipher, lowerCase))
    upperTransformedDict = dict(zip(upperCaseCipher, upperCase))

    monoPlaintext = ""
    for i in ciphertext:
        try:
            monoPlaintext += lowerTransformedDict[i]
        except(KeyError):
            try:
                monoPlaintext += upperTransformedDict[i]
            except(KeyError):
                monoPlaintext += i
    
    return monoPlaintext

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('cipher', choices=['caesar', 'affine', 'mono'])
    parser.add_argument('file')
    parser.add_argument('mode', choices=['e', 'd'])
    
    parser.add_argument('-s', '--shift', type=int)
    parser.add_argument('-a', '--a', type=int)
    parser.add_argument('-b', '--b', type=int)
    parser.add_argument('-k', '--key', type=str)

    args = parser.parse_args()

    with open(args.file, 'r') as input_file:
        plaintext = input_file.read()

    if args.cipher == 'caesar':
        if args.mode == 'e':
            if args.shift is not None:
                result = encrypt_caesar(plaintext, args.shift)
                print(result)
            else:
                print("Shift value is required for encryption with Caesar Cipher.")
        else:
            if args.shift is not None:
                result = decrypt_caesar(plaintext, args.shift)
                print(result)
            else:
                print("Shift value is required for decryption with Caesar Cipher.")

    elif args.cipher == 'affine':
        if args.mode == 'e':
            if args.a is not None and args.b is not None:
                result = encrypt_affine(plaintext, args.a, args.b)
                print(result)
            else:
                print("A and B values are required for encryption with Affine Cipher.")
        else:
            if args.a is not None and args.b is not None:
                result = decrypt_affine(plaintext, args.a, args.b)
                print(result)
            else:
                print("A and B values are required for decryption with Affine Cipher.")

    elif args.cipher == 'mono':
        if args.mode == 'e':
            if args.key is not None:
                result = encrypt_mono(plaintext, args.key)
                print(result)
            else:
                print("Key alphabet is required for encryption with Mono-alphabetic Cipher.")
        else:
            if args.key is not None:
                result = decrypt_mono(plaintext, args.key)
                print(result)
            else:
                print("Key alphabet is required for decryption with Mono-alphabetic Cipher.")

if __name__ == '__main__':
    main()