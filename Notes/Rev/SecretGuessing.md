# Password Guessing

```
[0xf7fb9450]> pdf @main
┌ 296: int main (char **argv);
│           ; var int32_t var_2ah @ ebp-0x2a
│           ; var int32_t var_16h @ ebp-0x16
│           ; var int32_t var_12h @ ebp-0x12
│           ; var int32_t var_10h @ ebp-0x10
│           ; var int32_t var_9h @ ebp-0x9
│           ; var int32_t var_8h @ ebp-0x8
│           ; arg char **argv @ esp+0x54
│           0x5660b1ad      8d4c2404       lea ecx, [argv]
│           0x5660b1b1      83e4f0         and esp, 0xfffffff0
│           0x5660b1b4      ff71fc         push dword [ecx - 4]
│           0x5660b1b7      55             push ebp
│           0x5660b1b8      89e5           mov ebp, esp
│           0x5660b1ba      53             push ebx
│           0x5660b1bb      51             push ecx
│           0x5660b1bc      83ec30         sub esp, 0x30
│           0x5660b1bf      e8ecfeffff     call sym.__x86.get_pc_thunk.bx
│           0x5660b1c4      81c3302e0000   add ebx, 0x2e30
│           0x5660b1ca      c745ea68656c.  mov dword [var_16h], 0x6c6c6568 ; 'hell'
│           0x5660b1d1      66c745ee6f00   mov word [var_12h], 0x6f    ; 'o' ; 111
│           0x5660b1d7      83ec0c         sub esp, 0xc
│           0x5660b1da      8d8314e0ffff   lea eax, [ebx - 0x1fec]
│           0x5660b1e0      50             push eax
│           0x5660b1e1      e86afeffff     call sym.imp.puts           ; int puts(const char *s)
│           0x5660b1e6      83c410         add esp, 0x10
│           0x5660b1e9      83ec08         sub esp, 8
│           0x5660b1ec      8d45d6         lea eax, [var_2ah]
│           0x5660b1ef      50             push eax
│           0x5660b1f0      8d8323e0ffff   lea eax, [ebx - 0x1fdd]
│           0x5660b1f6      50             push eax
│           0x5660b1f7      e864feffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
│           0x5660b1fc      83c410         add esp, 0x10
│           0x5660b1ff      83ec0c         sub esp, 0xc
│           0x5660b202      8d45d6         lea eax, [var_2ah]
│           0x5660b205      50             push eax
│           0x5660b206      e845feffff     call sym.imp.puts           ; int puts(const char *s)
│           0x5660b20b      83c410         add esp, 0x10
│           0x5660b20e      83ec0c         sub esp, 0xc
│           0x5660b211      8d45ea         lea eax, [var_16h]
│           0x5660b214      50             push eax
│           0x5660b215      e836feffff     call sym.imp.puts           ; int puts(const char *s)
│           0x5660b21a      83c410         add esp, 0x10
│           0x5660b21d      83ec08         sub esp, 8
│           0x5660b220      6a14           push 0x14                   ; 20
│           0x5660b222      8d8326e0ffff   lea eax, [ebx - 0x1fda]
│           0x5660b228      50             push eax
│           0x5660b229      e812feffff     call sym.imp.printf         ; int printf(const char *format)
│           0x5660b22e      83c410         add esp, 0x10
│           0x5660b231      c645f701       mov byte [var_9h], 1
│           0x5660b235      c745f0000000.  mov dword [var_10h], 0
│       ┌─< 0x5660b23c      eb54           jmp 0x5660b292
│      ┌──> 0x5660b23e      8d55d6         lea edx, [var_2ah]
│      ╎│   0x5660b241      8b45f0         mov eax, dword [var_10h]
│      ╎│   0x5660b244      01d0           add eax, edx
│      ╎│   0x5660b246      0fb600         movzx eax, byte [eax]
│      ╎│   0x5660b249      0fbed0         movsx edx, al
│      ╎│   0x5660b24c      8d4dea         lea ecx, [var_16h]
│      ╎│   0x5660b24f      8b45f0         mov eax, dword [var_10h]
│      ╎│   0x5660b252      01c8           add eax, ecx
│      ╎│   0x5660b254      0fb600         movzx eax, byte [eax]
│      ╎│   0x5660b257      0fbec0         movsx eax, al
│      ╎│   0x5660b25a      83ec04         sub esp, 4
│      ╎│   0x5660b25d      52             push edx
│      ╎│   0x5660b25e      50             push eax
│      ╎│   0x5660b25f      8d832ae0ffff   lea eax, [ebx - 0x1fd6]
│      ╎│   0x5660b265      50             push eax
│      ╎│   0x5660b266      e8d5fdffff     call sym.imp.printf         ; int printf(const char *format)
│      ╎│   0x5660b26b      83c410         add esp, 0x10
│      ╎│   0x5660b26e      8d55ea         lea edx, [var_16h]
│      ╎│   0x5660b271      8b45f0         mov eax, dword [var_10h]
│      ╎│   0x5660b274      01d0           add eax, edx
│      ╎│   0x5660b276      0fb610         movzx edx, byte [eax]
│      ╎│   0x5660b279      8d4dd6         lea ecx, [var_2ah]
│      ╎│   0x5660b27c      8b45f0         mov eax, dword [var_10h]
│      ╎│   0x5660b27f      01c8           add eax, ecx
│      ╎│   0x5660b281      0fb600         movzx eax, byte [eax]
│      ╎│   0x5660b284      38c2           cmp dl, al
│     ┌───< 0x5660b286      7406           je 0x5660b28e
│     │╎│   0x5660b288      c645f700       mov byte [var_9h], 0
│    ┌────< 0x5660b28c      eb0c           jmp 0x5660b29a
│    │└───> 0x5660b28e      8345f001       add dword [var_10h], 1
│    │ ╎│   ; CODE XREF from main @ 0x5660b23c
│    │ ╎└─> 0x5660b292      8b45f0         mov eax, dword [var_10h]
│    │ ╎    0x5660b295      83f805         cmp eax, 5                  ; 5
│    │ └──< 0x5660b298      76a4           jbe 0x5660b23e
│    │      ; CODE XREF from main @ 0x5660b28c
│    └────> 0x5660b29a      807df700       cmp byte [var_9h], 0
│       ┌─< 0x5660b29e      7414           je 0x5660b2b4
│       │   0x5660b2a0      83ec0c         sub esp, 0xc
│       │   0x5660b2a3      8d8331e0ffff   lea eax, [ebx - 0x1fcf]
│       │   0x5660b2a9      50             push eax
│       │   0x5660b2aa      e891fdffff     call sym.imp.printf         ; int printf(const char *format)
│       │   0x5660b2af      83c410         add esp, 0x10
│      ┌──< 0x5660b2b2      eb12           jmp 0x5660b2c6
│      │└─> 0x5660b2b4      83ec0c         sub esp, 0xc
│      │    0x5660b2b7      8d833ce0ffff   lea eax, [ebx - 0x1fc4]
│      │    0x5660b2bd      50             push eax
│      │    0x5660b2be      e87dfdffff     call sym.imp.printf         ; int printf(const char *format)
│      │    0x5660b2c3      83c410         add esp, 0x10
│      │    ; CODE XREF from main @ 0x5660b2b2
│      └──> 0x5660b2c6      b800000000     mov eax, 0
│           0x5660b2cb      8d65f8         lea esp, [var_8h]
│           0x5660b2ce      59             pop ecx
│           0x5660b2cf      5b             pop ebx
│           0x5660b2d0      5d             pop ebp
│           0x5660b2d1      8d61fc         lea esp, [ecx - 4]
└           0x5660b2d4      c3             ret
```