import requests

cookies = {'session_id': 'xyz123abc'}
resposta = requests.get('https://api.github.com', cookies=cookies)