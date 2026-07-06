import requests

payload = {'nome': 'Ana', 'idade': '28'}
response = requests.put('https://httpbin.org/put', data=payload)
print(response.json())