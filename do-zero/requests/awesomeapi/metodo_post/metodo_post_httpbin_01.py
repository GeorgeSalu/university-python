import requests

# requisição simples
response = requests.post('https://httpbin.org/post')
print(response.json())