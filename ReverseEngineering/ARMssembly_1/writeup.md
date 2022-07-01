# ARMssembly_1

## Given 
- An ARM assembly code "chall_1.S"
- The variables I got are 58, 2, 3

## Process
* Study the assembly code (I wrote some comments in my version of chall_1.S to help you understand all those crazy registers and memory. Take a look if you are new to assembly)
* The `main` should read an arg and pass it to `func`
* `func` returns the result of 58 * (2^2) / 3 - arg to `main`
* If the result == 0, then program will print 'win'

## Solution
- We need to know what arg should we pass in to get the program to print 'win', which we know now that is 77.
- Find the hex of 77 and fill it up to 4 bytes

## Flag
> picoCTF{0000004D}