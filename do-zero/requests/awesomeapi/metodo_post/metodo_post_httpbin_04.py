import requests

# Autenticação Básica
# Envia credenciais de usuário (usuário e senha) no cabeçalho da requisição.
response = requests.post('https://httpbin.org/post', auth=('user', 'pass'))
print(response.status_code)
print(response.json())
print(response.json()["headers"]["Authorization"])