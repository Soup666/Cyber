# Level 2

```c++
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char * argv[]){
    char buf[128];

    if(argc == 1){
        printf("Usage: %s argument\n", argv[0]);
        exit(1);
    }
    strcpy(buf,argv[1]);
    printf("%s", buf);

    return 0;
}
```
lets overwrite the buffer

we can use gdb to see the return address we're overwritin:
```bash
(gdb) run $(python -c 'print 132 * "A" + "BBBB"')
Starting program: /narnia/narnia2 $(python -c 'print 132 * "A" + "BBBB"')

Program received signal SIGSEGV, Segmentation fault.
0x42424242 in ?? ()
``` 

ehhh lets take a break