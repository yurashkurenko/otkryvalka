import requests
pload = {"Accept":"application/json","Content-Type":"application/json","Authorization":"Bearer "}
url="https://edge.qiwi.com/payment-history/v2/persons/79054725000/payments?rows=50"
r = requests.get(url,headers=pload)

print(r.json())

#requests.get(url, params=None, headers=None, cookies=None, auth=None, timeout=None)

#s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
