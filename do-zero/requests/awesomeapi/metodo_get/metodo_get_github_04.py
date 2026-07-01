import requests

# Enviando Cabeçalhos (Headers)
cabecalhos = {'User-Agent': 'MeuScriptPython/1.0'}
resposta = requests.get('https://api.github.com', headers=cabecalhos)
print(resposta.text)