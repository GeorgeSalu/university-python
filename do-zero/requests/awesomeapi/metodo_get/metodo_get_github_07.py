import requests

try:
    resposta = requests.get('https://api.github.com', timeout=2.5)
except requests.exceptions.Timeout:
    print('A requisição demorou demais.')