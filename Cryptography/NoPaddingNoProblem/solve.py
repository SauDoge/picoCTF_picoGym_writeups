from sys import byteorder
from pwn import *
from Crypto.Util.number import *


r = remote("mercury.picoctf.net",  28517)

r.recvuntil(b"n:")
n = r.recvline().strip()
r.recvuntil(b"e:")
e = r.recvline().strip()
r.recvuntil(b"ciphertext:")
c = r.recvline().strip()

# it is not going to decrypt c directly
# what about c + n


c = bytes_to_long(c)
print(c ,type(c))

n = bytes_to_long(n)
print(n, type(n))

new_cipher = c + n 
print(new_cipher, type(new_cipher))

r.interactive()