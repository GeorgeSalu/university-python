import requests

# Adiciona cabeçalhos (como tokens de autorização ou tipo de conteúdo) à requisição
headers = {'Authorization': 'Bearer SEU_TOKEN', 'Accept': 'application/json'}
response = requests.post('https://httpbin.org/post', headers=headers)
print(response.status_code)
print(response.json())