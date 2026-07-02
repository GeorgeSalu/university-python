import requests

# Definindo Cookies
cookies = {'session_id': 'xyz123abc'}
resposta = requests.get('https://api.github.com', cookies=cookies)
print(resposta.text)