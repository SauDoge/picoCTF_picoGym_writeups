cipher = "UFJKXQZQUNB"
key =  "SOLVECRYPTO"


# A = 0
# Z = 25
# ord(A) = 65


f = open("table.txt", "r")

f.readline()
f.readline()
lines = f.readlines()


array = []
for line in lines:
    line = line.strip().split(" ")
    array.append(line)

plaintext = ""
counter = 0
for char in key:
    offset = ord(char) - ord("A")
    print("Index of key ", char, " = ", offset)
    index = array[offset].index(cipher[counter])
    index -= 2
    print("Index of cipher", cipher[counter], " = ", index)

    p_offset = ord("A") + index
    plaintext += chr(p_offset)
    counter += 1

print(plaintext)



