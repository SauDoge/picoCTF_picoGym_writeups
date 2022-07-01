# Crackme-py

## Given
- A python script named 'crackme.py'

## Process
* Execute the script and it is a simple script that asks for two number input and return the larger
* That appears to be a smoke screen
* The actual function is to decypher `bezos_cc_secret`
* With the comments in `decode_secret()`, it appears that the cyphertext is encrypted in ROT47

## Solution
* Modify the script and execute the function `decode_secret(bezos_cc_secret)`

## Flag 
> picoCTF{1|\/|_4_p34|\|ut_502b984b}