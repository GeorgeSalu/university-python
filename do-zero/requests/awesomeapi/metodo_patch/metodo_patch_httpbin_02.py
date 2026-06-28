import requests

url = "https://httpbin.org/patch"
dados = {"status": "atualizado", "prioridade": 2}

# O requests converte automaticamente o dicionário para form-urlencoded
resposta = requests.patch(url, data=dados)

print(resposta.json())