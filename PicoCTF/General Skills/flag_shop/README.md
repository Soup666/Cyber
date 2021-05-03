# flag_shop

```
Author: Danny
Description

There's a flag shop selling stuff, can you buy a flag? Source. Connect with nc jupiter.challenges.picoctf.org 9745.
```
This was a fun challenge. I originally went after fflush(stdin) because a quick google search said it was exploitable. However this lead nowhere. So instead i tried to overflow the signed int to be negative. If we can minus a negative value, it will add to the total

we can see the program is in C so the default int size is 32 bits. The largest int for 32 bits is 2147483647. entering this when buying a flag gives us -900. Great! 

Here's how i think this works. 2147483647 in binary is 01111111111111111111111111111110, which is 33 bits long. since the buffer is 32 bit, it cuts off the first digit. Making it 1111111111111111111111111111110, which is -2.

Note how 1111111111111111111111111111100 is -4. so as the original value gets smaller, so does the signed verson if that makes sense

I sorta get it. Fun challenge!

#Flag
```
YOUR FLAG IS: picoCTF{m0n3y_bag5_65d67a74}
```