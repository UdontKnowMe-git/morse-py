charDict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
rawText = list(charDict.keys())
rawMorse = list(charDict.values())
class Encoder:
    def def_Encode(inp):
        encodedMorse = []
        for char in inp:
            if char.isalpha():
                encodedMorse.append(charDict[char.upper()])
            elif char in charDict:
                encodedMorse.append(charDict[char])
            elif char == " ":
                encodedMorse.append(" ")
            else:
                print(f"Unrecognized character {char} in input. Kindly try again with valid characters.")
                print("For a list of valid characters, input 'EncodingScheme' or 'EncSch'.")
        return " ".join(encodedMorse)
   
    def fileEncode(filename):
        decodedLines = filename.readlines()
        encodedLines = []
        for line in decodedLines:
            tempLine = []
            for char in line:
                if char.isalpha():
                    tempLine.append(charDict[char.upper()])
                elif char in charDict:
                    tempLine.append(charDict[char])
                elif char == " ":
                    tempLine.append(" ")
                else:
                    print(f"Unrecognized character '{char}' in input. Ignoring the invalid character.")
                    print("For a list of valid characters, input 'EncodingScheme' or 'EncSch'.")
            encodedLines.append(" ".join(tempLine))
        return encodedLines,decodedLines

class Decoder:
    def def_Decode(inp):
        decodedText = []
        for char in inp.split(" "):
            if char in rawMorse:
                decodedText.append(rawText[rawMorse.index(char)])
            elif char == "":
                decodedText.append(" ")
            else:
                print(f"Unrecognized character {char} in input. Kindly try again with valid characters.")
                print("For a list of valid characters, input 'EncodingScheme' or 'EncSch'.")
        return "".join(decodedText)

    def fileDecode(filename):
        encodedLines = filename.readlines()
        decodedLines = []
        for line in encodedLines.split(" "):
            decodedText = []
            for char in line:
                if char in rawMorse:
                    decodedText.append(rawText[rawMorse.index(char)])
                elif char == "":
                    decodedText.append(" ")
                else:
                    print(f"Unrecognized character {char} in input. Kindly try again with valid characters.")
                    print("For a list of valid characters, input 'EncodingScheme' or 'EncSch'.")
            decodedLines.append(" ".join(decodedText))
        return decodedLines,encodedLines