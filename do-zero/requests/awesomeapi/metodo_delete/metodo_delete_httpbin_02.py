import requests

# Enviando dados como Dicionário (Formulário)
url = "https://httpbin.org/delete"
dados = {"status": "atualizado", "prioridade": 2}

# O requests converte automaticamente o dicionário para form-urlencoded
resposta = requests.delete(url, data=dados)

print(resposta.json())