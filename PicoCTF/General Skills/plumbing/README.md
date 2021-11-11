# plumbing

Author: Alex Fulton/Danny Tunitis
Description

Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to jupiter.challenges.picoctf.org 4427.

# Solution

```bash
nc jupiter.challenges.picoctf.org 4427 > output.txt
cat output.txt | grep '{'
```

# Flag

`picoCTF{digital_plumb3r_5ea1fbd7}`