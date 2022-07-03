# Safe-opener

## Given 
- A Java file 'SafeOpener.java'

## Process
- Execute the java program and it requires a password
- According to the description, the password is the body of the Flag
- The password we entered will first be converted to byte array with `getBytes()`.
- Then it will be encoded to String with base64 using `encodedToString()`
- The encoded password is expected to be equal to "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz"

## Solution
- All we need to do is to revert the encoding process and apply it to "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz".
- Here is a snippet I add to `openSafe()` to print the original password:
```Java
String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
Base64.Decoder decoder = Base64.getDecoder();
String result = new String(decoder.decode(encodedkey));
System.out.println(result);
```

## Flag
> picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}