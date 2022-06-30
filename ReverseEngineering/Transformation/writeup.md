# Transformation

## Given
- a text file 'enc' with the string "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽"
- a clue of the following:
```Python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```


## Process
* The cypher text file contains chinese characters that have no particular meaning.
* The clue given looks like a piece of Python code which does the following:
    * For every two characters in a list called 'flag'
        * Take the Unicode of the first character and shift it to left by 8 bits
        * Take the Unicode of the second character 
        * Add them together to form a new Unicode and return the corresponding letter
    * Join the letters together
* The text file appears to be containing the result of the above 
process

## Solution Explanation
* A Chinese character can only be represented by UTF-16 with 16 bits, while an English letter can be represented by UTF-8 with 8 bits.
* The above process is taking two 8-bits and turn into a 16-bit.
* Therefore by:
    * Figuring out the 16-bit of every character in the cypher
    * Spliting them in half to obtain two 8-bits, 
    * Convert each 8-bit to English character
    
    we should obtain the original plaintext

## Flag
> picoCTF{16_bits_inst34d_of_8_75d4898b}


 