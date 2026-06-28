import requests

url = "https://httpbin.org/patch"
payload = {"titulo": "Novo Titulo", "ativo": True}

resposta = requests.patch(url, json=payload)

print(resposta.json())