import requests

# Adicionando Headers Personalizados
# Adiciona cabeçalhos (como tokens de autorização ou tipo de conteúdo) à requisição
headers = {'Authorization': 'Bearer SEU_TOKEN', 'Accept': 'application/json'}
payload = {'mensagem': 'Olá'}
response = requests.post('https://httpbin.org/post', headers=headers, data=payload)
print(response.status_code)
print(response.json())