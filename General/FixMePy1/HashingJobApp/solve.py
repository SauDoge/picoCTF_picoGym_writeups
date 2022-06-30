import hashlib
from pwn import *

host = remote("saturn.picoctf.net",64710)


for i in range(3):
    abc = host.recvuntil(b": '")
    print(abc)

    text = host.recvuntil(b'\'')
    text.decode("utf-8")
    text = text[:-1]
    print(text)

    a = hashlib.md5(text)
    ans = bytes(a.hexdigest(), "utf-8")
    host.sendline(ans)

host.recvline()
host.recvline()
