# Speed And Feed

## Given 
- nc mercury.picoctf.net 20301

## Process
* First, I netcat the given address and it returns a bunch of unknown codes
* According to the hint, it is some sort of code used by [CNC machines](https://www.fictiv.com/articles/g-code-knowledge-is-key-to-mastering-any-cnc-machine), which is called g-code.
* We can try to execute the g-code to see what it returns with some [simulators](https://nraynaud.github.io/webgcode/). 

## Solution
* Netcat the address and pipe the output into a txt file.
* Copy the content to a g-code simulator
* The preview should show the flag

## Flag
> picoCTF{num3r1cal_c0ntr0l_68a8fe29}