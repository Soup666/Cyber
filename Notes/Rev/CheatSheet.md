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

`gcc -g -m32 -O0 -S main.c`
Generates Assembly code for main.c

`gcc -m32 -o main main.c`
Compiles main.c into an executable

`gcc -m32 -c main.s -o main.o && gcc -m32 main.o -o main`
Compiles assembly into an object file then into an executable

 - m32 means 32 bit
 - O0 means no optimisation. More human readable Assembly 
