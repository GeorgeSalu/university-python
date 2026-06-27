import requests

resposta = requests.get('https://api.github.com')
dados_json = resposta.json()
print(dados_json['current_user_url'])