import requests

# delete - requisição simples
url = "https://httpbin.org/delete"
resposta = requests.delete(url)

print(resposta.json())