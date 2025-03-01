import argparse

def dictionaryListing():
    dictFile = open("dictionary.txt", "r")
    dictList = [line.strip().lower() for line in dictFile.readlines()]

    return dictList

def codingDictionary():
    lowerCase = "abcdefghijklmnopqrstuvwxyz"
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = [i for i in range(26)]

    lowerDict = dict(zip(lowerCase, nums))
    upperDict = dict(zip(upperCase, nums))

    reverseLowerDict = {v: k for k, v in lowerDict.items()}
    reverseUpperDict = {v: k for k, v in upperDict.items()}

    return [lowerDict, reverseLowerDict, upperDict, reverseUpperDict]

def break_caesar(ciphertext):
    convertionDicts = codingDictionary()
    lowerConvertionDict = convertionDicts[0]
    reversedLowerConvertionDict = convertionDicts[1]
    upperConvertionDict = convertionDicts[2]
    reversedUpperConvertionDict = convertionDicts[3]

    hitCounts = []

    for rightShiftAmount in range(1,26):
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

        wordsPlaintext = caesarPlaintext.split(" ")
        wordsDictionary = dictionaryListing()

        hitCount = 0
        for word in wordsPlaintext:
            if (wordsDictionary.count(word.lower()) > 0):
                hitCount += 1
                
        hitCounts.append(hitCount)

    maxHit = max(hitCounts)
    breakingShiftAmount = hitCounts.index(maxHit) + 1

    caesarPlaintext = ""
    for i in ciphertext:
        try:
            positionLower = lowerConvertionDict[i]
            shiftedPositionLower = (positionLower + breakingShiftAmount) % 26
            caesarPlaintext += reversedLowerConvertionDict[shiftedPositionLower]
        except(KeyError):
            try:
                positionUpper = upperConvertionDict[i]
                shiftedPositionUpper = (positionUpper + breakingShiftAmount) % 26
                caesarPlaintext += reversedUpperConvertionDict[shiftedPositionUpper]
            except(KeyError):
                caesarPlaintext += i
    
    return caesarPlaintext


def break_affine(ciphertext):
    convertionDicts = codingDictionary()
    lowerConvertionDict = convertionDicts[0]
    upperConvertionDict = convertionDicts[2]
    lowerCase = "abcdefghijklmnopqrstuvwxyz"
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    firstFiveWordsCiphertext = ciphertext.split(" ")[:5]
    firstFiveWordsCiphertext = " ".join(firstFiveWordsCiphertext)

    hitCounts = []

    for a in range(1, 26):
        for b in range(26):
            transformedNums = [(((i*a)+b)%26) for i in range(26)]
            reversedLowerTransformedDict = dict(zip(transformedNums, lowerCase))
            reversedUpperTransformedDict = dict(zip(transformedNums, upperCase))

            affinePlaintext = ""
            for i in firstFiveWordsCiphertext:
                try:
                    affinePlaintext += reversedLowerTransformedDict[lowerConvertionDict[i]]
                except(KeyError):
                    try:
                        affinePlaintext += reversedUpperTransformedDict[upperConvertionDict[i]]
                    except(KeyError):
                        affinePlaintext += i
            
            cleanAffinePlaintext = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in affinePlaintext)
            wordsPlaintext = cleanAffinePlaintext.split()
            wordsDictionary = dictionaryListing()

            hitCount = 0
            for word in wordsPlaintext:
                if (wordsDictionary.count(word.lower()) > 0):
                    hitCount += 1

            hitCounts.append(hitCount)

    maxHit = max(hitCounts)
    theA = int((hitCounts.index(maxHit)) / 26) + 1
    theB = (hitCounts.index(maxHit)) % 26
    transformedNums = [(((i*theA)+theB)%26) for i in range(26)]
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


def break_mono(ciphertext):
    words = ciphertext.split(" ")
    threeLetterWords = []
    twoLetterWords = []
    for word in words:
        if (len(word) == 3):
            threeLetterWords.append(word.lower())
        elif (len(word) == 2):
            twoLetterWords.append(word.lower())

    twoLetterWordsFrequencyDict = {}
    for i in twoLetterWords:
        if i in twoLetterWordsFrequencyDict:
            twoLetterWordsFrequencyDict[i] += 1
        else:
            twoLetterWordsFrequencyDict[i] = 1

    possibleTwoLetterCipherWords = []
    for key in twoLetterWordsFrequencyDict:
        if (twoLetterWordsFrequencyDict[key] / len(twoLetterWords) > 0.08):
            possibleTwoLetterCipherWords.append(key)

    threeLetterWordsFrequencyDict = {}
    for i in threeLetterWords:
        if i in threeLetterWordsFrequencyDict:
            threeLetterWordsFrequencyDict[i] += 1
        else:
            threeLetterWordsFrequencyDict[i] = 1

    possibleThreeLetterCipherWords = []
    for key in threeLetterWordsFrequencyDict:
        if (threeLetterWordsFrequencyDict[key] / len(threeLetterWords) > 0.08):
            possibleThreeLetterCipherWords.append(key)

    lowerAlphabet = "abcdefghijklmnopqrstuvwxyz"
    lowerAlphabetList = []
    for i in lowerAlphabet:
        lowerAlphabetList.append(i)

    cleanedCiphertext = ''.join(char for char in ciphertext if char.isalpha() or char.isspace())
    letterCounts = [0 for i in range(26)]
    charCount = 0
    for char in cleanedCiphertext:
        if (lowerAlphabetList.count(char) > 0):
            letterCounts[lowerAlphabet.index(char)] += 1
            charCount += 1
    
    for i in letterCounts:
        i = i/charCount

    ciphertextFreqDict = dict(zip(lowerAlphabetList, letterCounts))
    transformedDict = {}
    transformedDict["e"] = lowerAlphabet[letterCounts.index(max(letterCounts))]

    for threeLetterWord in possibleThreeLetterCipherWords:
        if (threeLetterWord[-1] == transformedDict["e"]):
            for twoLetterWord in possibleTwoLetterCipherWords:
                if (twoLetterWord[0] == threeLetterWord[0]):
                    transformedDict["t"] = threeLetterWord[0]
                    transformedDict["h"] = threeLetterWord[1]
                    transformedDict["o"] = twoLetterWord[1]

    firstLetterFreqs = [0 for i in range(26)] 
    for word in words:
        try:
            firstLetterFreqs[lowerAlphabet.index(word.lower()[0])] += 1
        except:
            pass
    for i in range(len(firstLetterFreqs)):
        firstLetterFreqs[i] = firstLetterFreqs[i] / len(words)
    ciphertextFirstLetterFreqDict = dict(zip(lowerAlphabetList, firstLetterFreqs))
    possibleFirstLetters = [lowerAlphabet[firstLetterFreqs.index(i)] for i in sorted(firstLetterFreqs, reverse=True)[:2]]

    for i in possibleFirstLetters:
        if(i in transformedDict.values()):
            pass
        else:
            transformedDict["a"] = i

    firstLetters = []
    for i in possibleTwoLetterCipherWords:
        firstLetters.append(i[0])
    for i in firstLetters:
        if (firstLetters.count(i) > 1):
            transformedDict["i"] = i

    return transformedDict

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('cipher', choices=['caesar', 'affine', 'mono'])
    parser.add_argument('file')
    
    args = parser.parse_args()
    
    try:
        with open(args.file, 'r') as txtFile:
            ciphertext = txtFile.read()
    except FileNotFoundError:
        print(f"Error: The file '{args.file}' was not found.")
        return
    
    if args.cipher == 'caesar':
        plaintext = break_caesar(ciphertext)
    elif args.cipher == 'affine':
        plaintext = break_affine(ciphertext)
    elif args.cipher == 'mono':
        plaintext = break_mono(ciphertext)
    
    print(plaintext)

if __name__ == '__main__':
    main()
