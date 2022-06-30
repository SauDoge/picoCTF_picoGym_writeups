from pwn import *
import re

def binToAscii(cipher):
    ciphers = cipher.split()

    asciiString = ""
    for binary_value in ciphers:
        intOfWord = int(binary_value,2)
        asciiChar = chr(intOfWord)
        asciiString += asciiChar

    return asciiString 

def octToAscii(cipher):
    ciphers = cipher.split()

    asciiString = ""
    for dec_value in ciphers:
        asciiChar = chr(int(dec_value,8))
        asciiString += asciiChar

    return asciiString 

def hexToAscii(cipher):
    ciphers = re.findall('..', cipher)

    asciiString = ""
    for hex_value in ciphers:
        asciiChar = chr(int(hex_value,16))
        asciiString += asciiChar

    return asciiString 


r = remote("jupiter.challenges.picoctf.org", 29956)

# first run as binary
r.recvuntil(b'Please give the ')

cipher = r.recvuntil (b' as a word')

cipher = cipher.decode("utf-8")
cipher = cipher.replace(' as a word', '')

asciiString = binToAscii(cipher)
print(asciiString)
r.sendline(bytes(asciiString,'utf-8'))


# second run as oct
r.recvuntil(b'Please give me the  ')

cipher = r.recvuntil (b' as a word')

cipher = cipher.decode("utf-8")
cipher = cipher.replace(' as a word', '')
print(cipher)

asciiString = octToAscii(cipher)
print(asciiString)

r.sendline(bytes(asciiString,'utf-8'))

# third run as hex 

r.recvuntil(b'Please give me the ')

cipher = r.recvuntil (b' as a word')

cipher = cipher.decode("utf-8")
cipher = cipher.replace(' as a word', '')
print(cipher)

asciiString = hexToAscii(cipher)
print(asciiString)

r.sendline(bytes(asciiString,'utf-8'))



r.interactive()

