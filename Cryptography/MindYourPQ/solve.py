# RSA algorithm
# p and q are large prime number
# n = pq
# f(n) = (p-1)(q-1)
# e is co-prime with f(n) and 1 < e < f(n)
# (n, e) is the public key

# find d such de mod f(n) = 1

# Encryption:
# c = m^e mod n

# Decryption:
# m = c^d mod n 

from calendar import c
from cmath import e
from tkinter import E
from Crypto.Util.number import *

# find N 

c = 964354128913912393938480857590969826308054462950561875638492039363373779803642185
n = 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
e = 65537
p = 2434792384523484381583634042478415057961
q = 650809615742055581459820253356987396346063

fn = (p-1)*(q-1)
print(fn)
d = pow(int(e) , -1, fn)

print(d)

m = pow(c, d, n)
print(long_to_bytes(m))