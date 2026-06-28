import requests

# Definindo Autenticação Básica
resposta = requests.patch("https://httpbin.org/patch", auth=("usuario", "senha"))
print(resposta.status_code)