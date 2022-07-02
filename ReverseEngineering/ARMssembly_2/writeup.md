# ARMssembly_2

## Given 
- An ARM assembly code 'chall_2.Ｓ'
- argument: 1748687564

## Process
- Study the assembly code (I have made comments on the chall_2.S to help)
- The code seems to iterate a loop for argument number of times. Within each loop, it increments a variable by 3. The variable is initialized by 0 and returned after the loop

## Solution
- Multiple argument by 3 and get the hex of the Multiple
- Since the hex takes only 32 bits, we will keep the rightmost 32 bits

## Flag
> picoCTF{38b09064}