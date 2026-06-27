import requests

# Envio de Dados em JSON
# Ideal para trabalhar com APIs modernas que exigem o envio de objetos estruturados.
payload = {'titulo': 'Python', 'status': 'ativo'}
response = requests.post('https://httpbin.org/post', json=payload)
print(response.json())