import requests

dados = {"nome": "Python", "tipo": "Linguagem"}
resposta = requests.put("https://httpbin.org/put", json=dados)
print(resposta.json()["json"])
