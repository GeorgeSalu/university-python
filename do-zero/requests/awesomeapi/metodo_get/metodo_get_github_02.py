import requests

# Enviando Parâmetros de Query (URL)
parametros = {'q': 'python', 'sort': 'stars'}
resposta = requests.get('https://github.com', params=parametros)
print(resposta.url)
