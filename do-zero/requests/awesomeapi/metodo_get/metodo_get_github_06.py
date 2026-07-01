import requests

# Definindo Autenticação Básica
from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth('usuario', 'senha')
resposta = requests.get('https://api.github.com/user', auth=auth)
print(resposta.text)