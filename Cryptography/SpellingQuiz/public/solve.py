key_f = open("study-guide.txt", "r")

cipher = open("flag.txt", "r").readline()

# frequecy analysis
counter_array = []

for i in range(26):
    counter_array.append(0)

for line in key_f:
    line = line.strip()
    for char in line:
        offset = ord(char)-ord("a")
        counter_array[offset] += 1

alphabet = list('abcdefghijklmnopqrstuvwxyz')
dictionary = dict(zip(alphabet, counter_array))

print(dictionary)