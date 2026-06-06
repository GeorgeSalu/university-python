# Consultar uma API e ler a resposta JSON
# Converte os dados brutos recebidos para um formato manipulável em Python

import requests

response = requests.get("https://api.github.com")
dados = response.json()

print(dados["current_user_url"])