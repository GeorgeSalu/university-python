import requests

# requisição simples
response = requests.put('https://httpbin.org/put')
print(response.json())