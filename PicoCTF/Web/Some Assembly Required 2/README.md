# Some Assembly Required 2

```
Author: Sears Schulz
Description

http://mercury.picoctf.net:7319/index.html
```

Note: copying the `xakgK\5cNs9=8:9l1?im8i<89?00>88k09=nj9kimnu` from the chrome dev tools adds some hidden characters. So I curl `http://mercury.picoctf.net:7319/aD8SvhyVkb`, cat the file and copy `xakgK\Ns9=8:9l1?im8i<89?00>88k09=nj9kimnu` from the output

Putting the encoded string into cyberchef -> master, gives the flag. Cyberchef tells us the encoding is XOR by 8

# Flag:

picoCTF{15021d97ae0a401788600c815fb1caef}