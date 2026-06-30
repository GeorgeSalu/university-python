import requests

# request get basico
resposta = requests.get('https://api.github.com')
print(resposta.status_code)