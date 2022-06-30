template_key = "picoCTF{1n_7h3_|<3y_of_"

keyHash = "66b8e54339dc8b7ff42eb6ea4d95561c67ad1192de710700b57c98e47c8af4b5"

filling = ""
arr = [4,5,3,6,2,7,1,8]

for num in arr:
    filling += keyHash[num]

template_key += filling
template_key += '}'

print(template_key)