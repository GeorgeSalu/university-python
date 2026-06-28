import requests

# Enviando dados no formato JSON
# Ideal para APIs modernas REST. Utilize o argumento json em vez de data para que a biblioteca defina o cabeçalho Content-Type: application/json automaticamente.
url = "https://httpbin.org/patch"
payload = {"titulo": "Novo Titulo", "ativo": True}

resposta = requests.patch(url, json=payload)

print(resposta.json())