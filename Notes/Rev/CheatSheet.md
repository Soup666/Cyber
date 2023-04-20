# Cheatsheet

A big collection of useful commands + examples

## Compiling C with gcc

main.c
```sh
#include <stdio.h>
int main() {
   printf("Hello, World!");
   return 0;
}
```

`gcc -m32 -o main main.c`
Compiles main.c into an executable

`gcc -g -m32 -O0 -S main.c`
Generates Assembly code for main.c

`gcc -m32 -c main.s -o main.o && gcc -m32 main.o -o main`
Compiles assembly into an object file then into an executable

 - m32 means 32 bit
 - O0 means no optimisation. More human readable Assembly 
 - g generates debug info for gdb

## r2

Debugger program

Pointer is called `seek`

```sh
Usage r2 -dA [program name]
```
`dA` is shorthand for loading it manually and using `aaa`. Just analyises it

`> V` 
Visual Mode

`> afl`
Prints function list (useful for finding main). Stands for Analyise Function List

`> pdf @main`
Decompile main function into assembly

```sh
[0x7f7f1c8909c0]> pdf @main
            ; DATA XREF from entry0 @ 0x560f1e9f2064
┌ 31: int main (int argc, char **argv, char **envp);
│           0x560f1e9f2139      55             push rbp
│           0x560f1e9f213a      4889e5         mov rbp, rsp
│           0x560f1e9f213d      488d05c00e00.  lea rax, str.Hello_World ; 0x560f1e9f3004 ; "Hello World"
│           0x560f1e9f2144      4889c7         mov rdi, rax
│           0x560f1e9f2147      b800000000     mov eax, 0
│           0x560f1e9f214c      e8dffeffff     call sym.imp.printf     ; int printf(const char *format)
│           0x560f1e9f2151      b800000000     mov eax, 0
│           0x560f1e9f2156      5d             pop rbp
└           0x560f1e9f2157      c3             ret
```
Example output for a hello world C program when decomping main

`> db [hex address]`
Set breakpoint

`> dc`
Run program

`>dr`
Display registersdb 

`> p`
Change view -> right

`> u`
Change view -> left

`> axt`
Show cross references ( where current function is called )

### Find main is Visual Mode

`> aaa`
`> afl`
`> V`
`> :`
`> s main` - seek main
`enter`

