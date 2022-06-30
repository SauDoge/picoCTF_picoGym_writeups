cipher = [20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]


for i in range(len(cipher)):
    cipher[i] += 64

print(cipher[0])

a = list(map(lambda x: chr(x), cipher))
print(a)