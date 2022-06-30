import re
import string

cipher = "ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"

# ALPHABET = abcdefghijklmnop
# len(ALPHABET = 16)

ALPHABET = string.ascii_lowercase[:16]
LOWERCASE_OFFSET = ord("a")
# len(key) = 1

# the plaintext is encoded with b16 first
# two digits in b16 = one char in plaintext

# then perform shift with the key,
# which is an single alphabet

# the shift is the actually caesar cipher


# 1: brute-force key
def back(c, k):
    # purpose: find c in shift()
    t2 = ord(k) - LOWERCASE_OFFSET
    for number in range(len(ALPHABET)):
        if ALPHABET[(number + t2) % len(ALPHABET)] == c:
            return chr(number + LOWERCASE_OFFSET)  

# tested correct
def b16_decode(cipher):
    answer = ""
    pairs = re.findall("..", cipher)
    for pair in pairs:
        index0 = ALPHABET.index(pair[0])
        index1 = ALPHABET.index(pair[1])
        
        binaryText = ""
        binaryText += "{0:04b}".format(index0)
        binaryText += "{0:04b}".format(index1)
        binary = int(binaryText, 2)
        answer += chr(binary)
    return answer

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc


for possible in ALPHABET:
    plain = ""
    answer = ""

    # revert the shifting
    # something wrong here
    for character in cipher:
        plain += back(character, possible)

    # b16 decoding
    answer = b16_decode(plain)
    print("picoCTF{" + answer + "}")