from pwn import *

SQUARE_SIZE = 6


def generate_square(alphabet):
    assert len(alphabet) == pow(SQUARE_SIZE, 2)
    matrix = []
    for i, letter in enumerate(alphabet):
        if i % SQUARE_SIZE == 0:
            row = []
        row.append(letter)
        if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
            matrix.append(row)
    return matrix


def get_index(letter, matrix):
    for row in range(SQUARE_SIZE):
        for col in range(SQUARE_SIZE):
            if matrix[row][col] == letter:
                return (row, col)
    print("letter not found in matrix.")
    exit()


def decrypt_pair(pair, matrix):
    p1 = get_index(pair[0], matrix)
    p2 = get_index(pair[1], matrix)

    # if pair on the same row
    if p1[0] == p2[0]:
        return matrix[p1[0]][(p1[1] - 1) % SQUARE_SIZE] + matrix[p2[0]][(p2[1] - 1) % SQUARE_SIZE]
    # if pair on the same col
    elif p1[1] == p2[1]:
        return matrix[(p1[0] - 1) % SQUARE_SIZE][p1[1]] + matrix[(p2[0] - 1) % SQUARE_SIZE][p2[1]]
    # if pair on diagonal
    else:
        return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]

def decrypt_string(s, matrix):
    result = ""
    if len(s) % 2 == 0:
        plain = s
    else:
        plain = s + "0uxtb3w4kj26q9m8gioe7nvahplr5dy1fzcs"[0]
    for i in range(0, len(plain), 2):
        result += decrypt_pair(plain[i:i + 2], matrix)
    return result





r = remote("mercury.picoctf.net", 21003)

r.recvuntil(b'Here is the alphabet: ')
alphabet = r.recvline().strip().decode("utf-8")
print(alphabet)
r.recvuntil(b'Here is the encrypted message: ')
e = r.recvline().strip().decode("utf-8")
print(e, len(e))


table = generate_square(alphabet)
print(table)
plaintext = decrypt_string(e, table)
print(plaintext)


payload = bytes(plaintext, 'utf-8')
r.recvuntil(b'What is the plaintext message? ')
r.sendline(payload)

r.interactive()