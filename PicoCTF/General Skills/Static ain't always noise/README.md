# Static ain't always noise

Author: syreal
Description

Can you look at the data in this binary: static? This BASH script might help!

# Solution

```bash
chmod +x ltdis.sh
./ltdis.sh static
cat static.ltdis.strings.txt | grep 'picoCTF'
```
this script attempts to recompile an executable from a hex dump. it saves the strings to a seperate file from the executable. in these strings is the flag!

# Flag

`picoCTF{d15a5m_t34s3r_6f8c8200}`