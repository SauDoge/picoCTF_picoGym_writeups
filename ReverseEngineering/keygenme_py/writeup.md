#  Keygenme-py

## Given 
- a python file named keygenme-trial.py

## Process
* Execute the python script
* It appears that we need to enter the correct license key, which the license key should be in form of 
> picoCTF{1n_7h3_|<3y_of_xxxxxxxx}
* We need to find what **xxxxxxxx** is

## Solution
* After looking into function `checkKey()`, we know that xxxxxxxx should be equal to the sha256 hash of the variable`bUsername_trial` of certain indices ([4,5,3,6,2,7,1,8])
* I modified the original python script to print the hash and hardcode it to my solve.py
* Replace the xxxxxxxx with the subset of the hash
* The key will be the answer

## Flag
> picoCTF{1n_7h3_|<3y_of_e584b363}