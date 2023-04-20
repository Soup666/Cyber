# Simple C Example (Addition)

main.c
```c
#include <stdio.h>

int main(void) {
        printf("Hello World!\n");
        int a = 1;
        int b = 2;
        printf("%d + %d = %d\n", a, b, a+b);
        return 0;
}
```

```
[Output] 
Hello World!
1 + 2 = 3
```

Compile with `gcc`:

`gcc -g -m32 -o main main.c && ./main`

Running this in r2 we can get the assembly:

`r2 -dA main`
`> pdf @main`

```
106: int main (char **argv);
│           ; var int32_t var_10h @ ebp-0x10
│           ; var int32_t var_ch @ ebp-0xc
│           ; var int32_t var_8h @ ebp-0x8
│           ; arg char **argv @ esp+0x34
│           0x5661219d      8d4c2404       lea ecx, [argv]
│           0x566121a1      83e4f0         and esp, 0xfffffff0
│           0x566121a4      ff71fc         push dword [ecx - 4]
│           0x566121a7      55             push ebp
│           0x566121a8      89e5           mov ebp, esp
│           0x566121aa      53             push ebx
│           0x566121ab      51             push ecx
│           0x566121ac      83ec10         sub esp, 0x10
│           0x566121af      e8ecfeffff     call sym.__x86.get_pc_thunk.bx
│           0x566121b4      81c3402e0000   add ebx, 0x2e40
│           0x566121ba      83ec0c         sub esp, 0xc
│           0x566121bd      8d8314e0ffff   lea eax, [ebx - 0x1fec]
│           0x566121c3      50             push eax
│           0x566121c4      e887feffff     call sym.imp.puts           ; int puts(const char *s)
│           0x566121c9      83c410         add esp, 0x10
│           0x566121cc      c745f4010000.  mov dword [var_ch], 1
│           0x566121d3      c745f0020000.  mov dword [var_10h], 2
│           0x566121da      8b55f4         mov edx, dword [var_ch]
│           0x566121dd      8b45f0         mov eax, dword [var_10h]
│           0x566121e0      01d0           add eax, edx
│           0x566121e2      50             push eax
│           0x566121e3      ff75f0         push dword [var_10h]
│           0x566121e6      ff75f4         push dword [var_ch]
│           0x566121e9      8d8321e0ffff   lea eax, [ebx - 0x1fdf]
│           0x566121ef      50             push eax
│           0x566121f0      e84bfeffff     call sym.imp.printf         ; int printf(const char *format)
│           0x566121f5      83c410         add esp, 0x10
│           0x566121f8      b800000000     mov eax, 0
│           0x566121fd      8d65f8         lea esp, [var_8h]
│           0x56612200      59             pop ecx
│           0x56612201      5b             pop ebx
│           0x56612202      5d             pop ebp
│           0x56612203      8d61fc         lea esp, [ecx - 4]
└           0x56612206      c3             ret
```

# Goal 1 - Find Hello World in register

Steps:
 - find address of hello world printf
 - breakpoint on printf
 - find register with string
 - display register

We can find the address using `pdf @main`

```
0x565d51af      e8ecfeffff     call sym.__x86.get_pc_thunk.bx
0x565d51b4      81c3402e0000   add ebx, 0x2e40
0x565d51ba      83ec0c         sub esp, 0xc
0x565d51bd      8d8314e0ffff   lea eax, [ebx - 0x1fec]
0x565d51c3      50             push eax
0x565d51c4      e887feffff     call sym.imp.puts           ; int puts(const char *s)
```

Here we can see `0x565d51c4` is the address we want to break point on. We can do that using `db 0x565d51c4`. Next we run with `dc`. We can check we hit the breakpoint by running `pdf @main` again and the line will be highlighted. Here we can see the call before the print is `push eax`, so we can assume the string will be in the `eax` register.

We can display the contents of `eax` with `px @eax`, and we get:

```
[0x565d51c4]> px @eax
- offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x565d6008  4865 6c6c 6f20 576f 726c 6421 0025 6420  Hello World!.%d 
0x565d6018  2b20 2564 203d 2025 640a 0000 011b 033b  + %d = %d......;
0x565d6028  2800 0000 0400 0000 fcef ffff 7000 0000  (...........p...
0x565d6038  3cf0 ffff 9400 0000 4cf0 ffff 4400 0000  <.......L...D...
0x565d6048  79f1 ffff a800 0000 1400 0000 0000 0000  y...............
0x565d6058  017a 5200 017c 0801 1b0c 0404 8801 0708  .zR..|..........
0x565d6068  1000 0000 1c00 0000 00f0 ffff 2c00 0000  ............,...
0x565d6078  0000 0000 1400 0000 0000 0000 017a 5200  .............zR.
0x565d6088  017c 0801 1b0c 0404 8801 0000 2000 0000  .|.......... ...
0x565d6098  1c00 0000 84ef ffff 4000 0000 000e 0846  ........@......F
0x565d60a8  0e0c 4a0f 0b74 0478 003f 1a3b 2a32 2422  ..J..t.x.?.;*2$"
0x565d60b8  1000 0000 4000 0000 a0ef ffff 0800 0000  ....@...........
0x565d60c8  0000 0000 3000 0000 5400 0000 c9f0 ffff  ....0...T.......
0x565d60d8  6a00 0000 0044 0c01 0049 1005 0275 0042  j....D...I...u.B
0x565d60e8  0f03 7578 0610 0302 757c 0255 c10c 0100  ..ux....u|.U....
0x565d60f8  41c3 41c5 430c 0404 0000 0000 0000 0000  A.A.C...........
```

There we go! Hello World in the register `eax`.