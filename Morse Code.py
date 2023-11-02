MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
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
def encrypt(message):
    encrypted= ""
    for letter in message:
        if letter != " ":
            encrypted += MORSE_CODE_DICT[letter] + " "
        else:
            encrypted += " "
    return encrypted

inv_map = {a: b for b,a in MORSE_CODE_DICT.items()}

def decrypt(message):
    decrypted = ""
    word = ""
    for code in message:
        if code != " ":
            word += code
            i = 0
        else:
            i+=1
            if i == 2:
                decrypted += " "
            else:
                decrypted += inv_map[word]
                word = ""
    return decrypted


message = "GEEKS-FOR-GEEKS"
result = encrypt(message.upper())
print (result)
 
message = "--. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ... "
result = decrypt(message)
print (result)
 





            
