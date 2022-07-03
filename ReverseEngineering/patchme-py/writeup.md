# Patchme-py

## Given
- A python file 'patchme.flag.py'
- A enc file 'flag.txt.enc'

## Process
- Suggested by the description, I execute the python script with the enc file in the same directory
- The script asked for an input for the correct password.
- It appears from the source code that the flag in the enc file will be decoded and printed if we get the password correct.

## Solution
We have two solutions:
### 1. Intuitive Solution
* The validation of the password is done by `level_1_pw_check()`, where the criteria is hardcoded in the if-statement.
```python
    if( user_pw == "ak98" + \
                   "-=90" + \
                   "adfjhgj321" + \
                   "sleuth9000"):
```
* You can fetch the password directly and enter the password to the program.
* It should return the full flag.

### 2. Patching
* Since the name of this challenge is 'Patchme.py', we can also patch the file to get the job done.
*  Since the display of the true flag only depends on the following code:
``` Python
decryption = str_xor(flag_enc.decode(), "utilitarian")
print(decryption)
```
* We can remove other lines in `level_1_pw_check()` but the above two.
* Once we re-execute the file, the flag should be printed.
## Flag
> picoCTF{p47ch1ng_l1f3_h4ck_c4a4688b}