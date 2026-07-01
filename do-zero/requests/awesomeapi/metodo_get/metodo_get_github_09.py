import requests

# Isso permite inspecionar manualmente a resposta de redirecionamento
resposta = requests.get('http://github.com', allow_redirects=False)
print(resposta.status_code)