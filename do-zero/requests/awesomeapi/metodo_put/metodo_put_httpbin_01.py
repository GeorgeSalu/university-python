import requests

# post simples
response = requests.put('https://httpbin.org/put')
print(response.json())