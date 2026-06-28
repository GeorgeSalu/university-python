import requests

cabecalhos = {"Authorization": "Bearer meu_token_secreto", "Content-Type": "application/json"}
resposta = requests.put(
    "https://httpbin.org/put", headers=cabecalhos, json={"ativo": True}
)
print(resposta.json()["headers"]["Authorization"])