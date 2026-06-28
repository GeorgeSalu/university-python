import requests

# patch - requisição simples
url = "https://httpbin.org/patch"
resposta = requests.patch(url)

print(resposta.json())