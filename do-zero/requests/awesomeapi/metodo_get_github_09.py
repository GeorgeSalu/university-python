import requests

resposta = requests.get('http://github.com', allow_redirects=False)
print(resposta.status_code)