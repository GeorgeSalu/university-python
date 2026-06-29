import requests

# Cabeçalhos (Headers)
# Adiciona chaves de autenticação ou filtros na URL junto com os dados modificados.
url = "https://httpbin.org/patch"
meus_headers = {"Authorization": "Bearer SEU_TOKEN_AQUI"}

resposta = requests.patch(url, headers=meus_headers)

print("Status Code:", resposta.status_code)
print("Dados recebidos pelo servidor:", resposta.json())