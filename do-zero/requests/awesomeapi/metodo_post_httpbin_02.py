import requests

payload = {'nome': 'Ana', 'idade': '28'}
response = requests.post('https://httpbin.org/post', data=payload)
print(response.json())