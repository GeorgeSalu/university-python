import requests

# Autenticação Básica (HTTP Basic Auth)
# Envia credenciais de usuário e senha de forma padrão.
resposta = requests.put(
    "https://httpbin.org/put", auth=("usuario_teste", "senha123")
)
print(resposta.status_code)
print(resposta.json())
print(resposta.json()["headers"]["Authorization"])