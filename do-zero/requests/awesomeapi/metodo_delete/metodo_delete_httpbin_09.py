import requests

# Definindo Autenticação Básica
resposta = requests.delete("https://httpbin.org/delete", auth=("usuario", "senha"))
print(resposta.json())
print(resposta.status_code)
print(resposta.status_code)
print(resposta.json())
print(resposta.json()["headers"]["Authorization"])