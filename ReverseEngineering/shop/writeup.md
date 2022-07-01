# Shop

## Given 
* a ELF file 'source'
* nc mercury.picoctf.net 37799

## Process
* Execute the source file and observe what it does.
* The flag should be in the item "Fruitful Flag", but we don't have enough coins to buy it
* The hint says we need to beware of edge cases, therefore I tried to input different test cases to the program:
    * extremely large numbers
    * 0
    * negative numbers
    * non-numbers
* It turns out that if we buy a negative amount of items, our coin will increase. It is likely that the input is not being validate before computating the coins.

## Solution
* In the terminal, nc mercury.picoctf.net 37799
* Buy a random item with negative quantity until we have 100 coins
* Buy the Fruitful Flag
* It returns an array of integer, which looks like ASCII code
* Decode the ASCII code to characters with `chr()` in python

## Flag
> picoCTF{b4d_brogrammer_591a895a}