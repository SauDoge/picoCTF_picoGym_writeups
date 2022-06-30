import codecs

f = open("ciphertext", "r")

cipher = f.readline()
cipher = cipher.replace("picoCTF{", "").replace("}", "")
def encrypt(plaintext, shift):
    result = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        if (char.isupper()):
            result += chr((ord(char)+ shift -65) %26 + 65)
        if (char.islower()):
            result += chr((ord(char)+ shift -97) %26 + 97)
    return result

for i in range(26):
    print("picoCTF{" + encrypt(cipher, i) + "}")