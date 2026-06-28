import requests

url = "https://httpbin.org/delete"
payload = {"titulo": "Novo Titulo", "ativo": True}

resposta = requests.delete(url, json=payload)

print(resposta.json())