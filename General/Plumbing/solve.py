from pwn import *

r = remote("jupiter.challenges.picoctf.org",4427)

line = r.recvline()

while True:
    line = line.decode('utf-8')
    if line.find("picoCTF{") != -1:
        print(line)
        break
    else:
        line = r.recvline()