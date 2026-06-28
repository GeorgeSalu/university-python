import requests

# Enviando dados no formato JSON
# Ideal para APIs modernas REST. Converte o dicionário automaticamente com json=
dados = {"nome": "Python", "tipo": "Linguagem"}
resposta = requests.put("https://httpbin.org/put", json=dados)
print(resposta.json()["json"])
