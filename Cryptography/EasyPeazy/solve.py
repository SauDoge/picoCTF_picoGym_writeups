# nc mercury.picoctf.net 41934

from pwn import *
import codecs

r = remote("mercury.picoctf.net", 41934)
r.recvline()
r.recvline()
encrypted_flag = r.recvline()

# find out how long is the flag
encrypted_flag = encrypted_flag.strip()
print(unhex(encrypted_flag))

print(encrypted_flag, type(encrypted_flag))
lenFlag = len(encrypted_flag) // 2
print(lenFlag)


# encrypt something that has length = 50000 - len(flag)
lenPayload = 50000 - lenFlag
payload = 'a' * lenPayload
print(len(payload))


# send the payload
r.recvuntil(b'What data would you like to encrypt? ')
r.sendline(bytes(payload,'ascii'))

# send the encrpyted flag for XOR
r.recvuntil(b'What data would you like to encrypt? ')
r.sendline(unhex(encrypted_flag))
r.interactive()


# try encrypt flag after one iteration
# supposedly it will xor and back to flag 