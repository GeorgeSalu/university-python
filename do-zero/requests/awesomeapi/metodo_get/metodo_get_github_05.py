import requests

# get imagem
resposta = requests.get('https://python.org')

with open('logo.png', 'wb') as arquivo:
    for chunk in resposta.iter_content(1024):
        arquivo.write(chunk)