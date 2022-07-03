## gdb-test-drive

## Given
- A ELF file 'gdbme'

## Process
- Execute the ELF directly will return nothing. It seems that the program is on pause.

## Solution
- As long as you follow the instructions from the description, you can get the flag

## Flag 
> picoCTF{d3bugg3r_dr1v3_197c378a}

## Remarks
I will explain more on what the instructions implied
- `(gdb) layout asm`: This displays the assembly and command window in the terminal together
- `(gdb) break *(main+99)`: This sets a breakpoint at address main + 99. 
- `(gdb) run`: This executes the program until the breakpoint
- `(gdb) jump *(main+104)`: This instruction will jump to the specified address and execute the paused program from there.
- In this case, the code on *(main+99) will be skipped, which appears to be a sleep function that causes the pause.

### More details:   
[GDB Manual](https://sourceware.org/gdb/current/onlinedocs/gdb/)