# Simple web

```
Time to warm up!
http://dctf1-chall-simple-web.westeurope.azurecontainer.io:8080
```

# Solution 

So clicking 'get flag' tells us we're not authorized. So how does it check? Checking cookies shows no values so lets check what request is being sent. Checking the paramters in the network POST request, we can see:
```json
data = {
  'flag': '1',
  'auth': '0',
  'Submit': 'Submit'
}
```
Changing auth to 1 and resending the request via my python script gave the flag!

# Flag: dctf{w3b_c4n_b3_fun_r1ght?}