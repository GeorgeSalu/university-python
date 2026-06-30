import requests

# query params
parametros = {'q': 'python', 'sort': 'stars'}
resposta = requests.get('https://github.com', params=parametros)
print(resposta.url)
