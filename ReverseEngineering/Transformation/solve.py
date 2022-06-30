with open('enc.txt', 'r') as f:
    cypher = f.readline()

plaintext = ""

for char in cypher:
    hexCode = hex(ord(char)).lstrip('0x')
    upper = bytes.fromhex(hexCode[0:2]).decode('UTF-8')
    lower = bytes.fromhex(hexCode[2:4]).decode('UTF-8')
    plaintext += upper
    plaintext += lower

print(plaintext)
    
    