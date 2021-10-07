import requests, pprint

headers = {
    'authority': 'cloudninebank.com',
    'sec-ch-ua': '"Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
    'sec-ch-ua-platform': '"Windows"',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': '*/*',
    'origin': 'https://play.cyberstart.com',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://play.cyberstart.com/',
    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
}

data = {
  'token': 'CNcsmXX5d50ZQCG5Us4twDi18awV'
}

response = requests.post('https://cloudninebank.com/get-accounts', headers=headers, data=data)
print(response)
pprint.pprint(response.json())