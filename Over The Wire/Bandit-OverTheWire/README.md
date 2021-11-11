# Writeups for bandit0

# level 0

``` bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
Password: bandit0
```

###### Flag: boJ9jbbUNNfktd78OOpsqOltutMc3MY1

# level 1

### Method 1

``` bash
chmod +x -
./-
./-: line 1: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9: command not found
```

### Method 2

``` bash
subl -
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

###### Flag: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

# level 2

``` bash
cat spaces\ in\ this\ filename
```

###### Flag: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

# level 3

``` bash
cat inhere/.hidden
```

###### Flag: pIwrPrtPN36QITSp3EQaw936yaFoFgAB

# level 4

```bash
file ./*

./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data

cat ./-file07 
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```

###### Flag: koReBOKuIDDepwhWk7jZC0RTdopnAYKh

# level 5

```bash
find . -exec ls -l {} \; | grep '952'
cat ./maybehere07/.file2
```

###### Flag: DXjZPULLxYr17uwoI01bNLQbtFemEgo7

# level 6

```bash
find . -group 'bandit6' -user 'bandit7'  2>/dev/null
./var/lib/dpkg/info/bandit7.password
cat ./var/lib/dpkg/info/bandit7.password
```

###### Flag: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

# level 7

``` bash
cat data.txt | grep 'millionth'
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

###### Flag: cvX2JJa4CFALtqS87jk27qwqGhBM9plV

# level 8

```bash
(uniq requires it to be piped through *sort* first)
sort data.txt |uniq -D
```

###### Flag: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

# level 9

```bash
strings data.txt | grep '=='
```

###### Flag: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

# level 10

```bash
cat data.txt | base64 -d
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```

###### Flag: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

# level 11

```bash
cat data.txt | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'
```

###### Flag: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

# level 12

``` bash
cat data.txt | xxd -r >new
then keep unzipping using *file* to find out the type
```

#### Flag: 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

# level 13

``` bash
scp -P 2220 bandit13@bandit.labs.overthewire.org:~/sshkey.private .
```

###### Flag: Private key

# level 14

``` bash
chmod 600 sshkey.private
ssh bandit14@bandit.labs.overthewire.org -p 2220 -i sshkey.private 
cat /etc/bandit_pass/bandit14
```

###### Flag: 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

# level 15

``` bash
Log on
nc localhost 30000
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
```

###### Flag: BfMYroe26WYalil77FoDi9qh59eK5xNr

# level 16

```bash
openssl s_client -connect localhost:30001
```

###### Flag: cluFn7wTiGryunymYOu4RcffSxQluehd


# level 17

```bash
nmap -sV localhost -p 31000-32000

PORT      STATE SERVICE     VERSION
31046/tcp open  echo
31518/tcp open  ssl/echo
31691/tcp open  echo
31790/tcp open  ssl/unknown
31960/tcp open  echo


openssl s_client -connect localhost:31790

-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----
```
# label 18

```bash
diff password.old password.new
```

###### Flag: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd

# level 19

```bash
scp -P 2220 bandit18@bandit.labs.overthewire.org:~/readme .
```

###### Flag: IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x


# level 20

``` bash
./bandit20-do cat /etc/bandit_pass/bandit20
```

###### Flag: GbKksEFF4yrVs6il55v6gwY5aVje5f0j

# level 21

```bash
nc -lnvp 8888
./suconnect 8888
```

###### Flag: gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr

# level 22

```bash
vi /etc/cron.d/cronjob_bandit22

@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null                                
 * * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null

cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv

cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

```

###### Flag: Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

# level 23

```bash
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null

cat /usr/bin/cronjob_bandit23.sh
```
```
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```
```
cat /tmp/8ca319486bfbbc3663ea0fbe81326349
```

###### Flag: jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n

# level 24

``` bash
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done

cd /tmp/Soup123/
touch password.txt
touch script.sh

#!/bin/bash

whoami > /tmp/Soup123/test
cat /etc/bandit_pass/bandit24 > /tmp/Soup123/pass.txt 2>/tmp/Soup123/error.txt

chmod 666 password.txt
```
###### Flag: UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

# level 25

``` bash
  1 import sys                                                                                
  2 import socket
  3 import time
  4  
  5 hostname = 'localhost'
  6 port = 30002
  7 has = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ'
  8 digit = 1000
  9  
 10 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 11 sock.connect(('localhost', 30002))
 12 def netcat(hn, p, content):
 13     global sock
 14     print(content)
 15     sock.sendall(content + '\n')
 16     data = sock.recv(1024)
 17     print(data)
 18     if ('Correct' in data):
 19         print('found')
 20         return
 21     #sock.shutdown(socket.SHUT_WR)
 22     time.sleep(0.5)
 23     return data
 24  
 25 for i in range(1000, 10000):
 26     c = has + ' ' + str(i)
 27     d = netcat(hostname, port, c)
 28     if ('Correct' in d):
 29         break
```

###### Flag: uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

# level 25 -> 26

```bash
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEApis2AuoooEqeYWamtwX2k5z9uU1Afl2F8VyXQqbv/LTrIwdW
pTfaeRHXzr0Y0a5Oe3GB/+W2+PReif+bPZlzTY1XFwpk+DiHk1kmL0moEW8HJuT9
/5XbnpjSzn0eEAfFax2OcopjrzVqdBJQerkj0puv3UXY07AskgkyD5XepwGAlJOG
xZsMq1oZqQ0W29aBtfykuGie2bxroRjuAPrYM4o3MMmtlNE5fC4G9Ihq0eq73MDi
1ze6d2jIGce873qxn308BA2qhRPJNEbnPev5gI+5tU+UxebW8KLbk0EhoXB953Ix
3lgOIrT9Y6skRjsMSFmC6WN/O7ovu8QzGqxdywIDAQABAoIBAAaXoETtVT9GtpHW
qLaKHgYtLEO1tOFOhInWyolyZgL4inuRRva3CIvVEWK6TcnDyIlNL4MfcerehwGi
il4fQFvLR7E6UFcopvhJiSJHIcvPQ9FfNFR3dYcNOQ/IFvE73bEqMwSISPwiel6w
e1DjF3C7jHaS1s9PJfWFN982aublL/yLbJP+ou3ifdljS7QzjWZA8NRiMwmBGPIh
Yq8weR3jIVQl3ndEYxO7Cr/wXXebZwlP6CPZb67rBy0jg+366mxQbDZIwZYEaUME
zY5izFclr/kKj4s7NTRkC76Yx+rTNP5+BX+JT+rgz5aoQq8ghMw43NYwxjXym/MX
c8X8g0ECgYEA1crBUAR1gSkM+5mGjjoFLJKrFP+IhUHFh25qGI4Dcxxh1f3M53le
wF1rkp5SJnHRFm9IW3gM1JoF0PQxI5aXHRGHphwPeKnsQ/xQBRWCeYpqTme9amJV
tD3aDHkpIhYxkNxqol5gDCAt6tdFSxqPaNfdfsfaAOXiKGrQESUjIBcCgYEAxvmI
2ROJsBXaiM4Iyg9hUpjZIn8TW2UlH76pojFG6/KBd1NcnW3fu0ZUU790wAu7QbbU
i7pieeqCqSYcZsmkhnOvbdx54A6NNCR2btc+si6pDOe1jdsGdXISDRHFb9QxjZCj
6xzWMNvb5n1yUb9w9nfN1PZzATfUsOV+Fy8CbG0CgYEAifkTLwfhqZyLk2huTSWm
pzB0ltWfDpj22MNqVzR3h3d+sHLeJVjPzIe9396rF8KGdNsWsGlWpnJMZKDjgZsz
JQBmMc6UMYRARVP1dIKANN4eY0FSHfEebHcqXLho0mXOUTXe37DWfZza5V9Oify3
JquBd8uUptW1Ue41H4t/ErsCgYEArc5FYtF1QXIlfcDz3oUGz16itUZpgzlb71nd
1cbTm8EupCwWR5I1j+IEQU+JTUQyI1nwWcnKwZI+5kBbKNJUu/mLsRyY/UXYxEZh
ibrNklm94373kV1US/0DlZUDcQba7jz9Yp/C3dT/RlwoIw5mP3UxQCizFspNKOSe
euPeaxUCgYEAntklXwBbokgdDup/u/3ms5Lb/bm22zDOCg2HrlWQCqKEkWkAO6R5
/Wwyqhp/wTl8VXjxWo+W+DmewGdPHGQQ5fFdqgpuQpGUq24YZS8m66v5ANBwd76t
IZdtF5HXs2S5CADTwniUS5mX1HO9l5gUkk+h0cH5JnPtsMCnAUM+BRY=
-----END RSA PRIVATE KEY-----

vim can be used to load another file using :e
```
###### Flag: 5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z

# level 26 -> 27

```bash
minimising the shell window runs the more command found in the previous level
using

 v

then

 :set shell=/bin/bash
 :!ls

shows us bandit27-do exists

 :!./bandit27-do cat /etc/bandit_pass/bandit27

gives

 3ba3118a22e93127a4ed485be72ef5ea

```

###### Flag: 3ba3118a22e93127a4ed485be72ef5ea

# level 27 -> 28

```bash
easy this one. mkdir in /tmp and cd to it. then run 

 git clone ssh://bandit27-git@localhost/home/bandit27-git/repo

using the password from  the last challenge to get the readme

 The password to the next level is: 0ef186ac70e04ea33b4c1853d2526fa2
```

###### Flag: 0ef186ac70e04ea33b4c1853d2526fa2

# level 28 -> 29

```bash
inside the github given is

 # Bandit Notes
 Some notes for level29 of bandit.

 ## credentials

 - username: bandit29
 - password: xxxxxxxxxx

using git log -p we can see the changes which gives us the password
```

###### Flag: bbc96594b4e001778eee9975372716b2

# level 29 -> 30

```bash
there is a branch which has the password in it. running

 git diff master origin/dev

gives us the password

NOTE:

running git checkout origin/dev also gives the password
```

###### Flag: 5b90576bedb2cc04c86a9e924ce42faf

# level 30 -> 31

```bash
 git tag --list
shows a secret tag
 git show secret
gives the password
```

###### Flag: 47e603bb428404d265f59c42920d81e5

# level 31 -> 32

```bash
 echo 'May I come in?' > key.txt
 git add key.txt -f
 git commit -am 'key'
 git push origin master
```

###### Flag: 56a9bf19c63d650ce78e6ec0354ee45e

# level 32 -> 33

```bash

```

###### Flag: