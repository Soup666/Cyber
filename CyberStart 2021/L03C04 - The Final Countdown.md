# The Final Countdown

This one was pretty simple. Made a script to make some web requests then submit the flag!

    import requests, pprint

    links = ['https://roambarcelona.com/clock-pt1?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D',
            'https://roambarcelona.com/clock-pt2?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D',
            'https://roambarcelona.com/clock-pt3?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D',
            'https://roambarcelona.com/clock-pt4?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D',
            'https://roambarcelona.com/clock-pt5?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D']

    headers = {
    }

    data = {
    }

    code = [requests.post(i, headers=headers, data=data).text for i in links]

    headers = {
        'authority': 'roambarcelona.com',
        'sec-ch-ua': '"Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://play.cyberstart.com/',
        'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
    }

    params = (
        ('verify', 'Na2Q+eqhSP5hTRLDwpTNoA=='),
        ('string', '<clock pts>'),
    )

    response = requests.get('https://roambarcelona.com/get-flag', headers=headers, params=params)

    #NB. Original query string below. It seems impossible to parse and
    #reproduce query strings 100% accurately so the one below is given
    #in case the reproduced version is not "correct".
    print(''.join(code))
    response = requests.get('https://roambarcelona.com/get-flag?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D&string=' + ''.join(code), headers=headers)

    print(response.text)
