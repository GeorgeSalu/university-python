import requests

# Envio de Dados Simples (Formulário)
# Envia dados de um formulário padrão codificado como application/x-www-form-urlencoded
payload = {'nome': 'Ana', 'idade': '28'}
response = requests.post('https://httpbin.org/post', data=payload)
print(response.json())