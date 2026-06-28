import requests

# Utilizando Sessão para Persistência
sessao = requests.Session()
sessao.headers.update({"X-App-Id": "XYZ"})
resposta = sessao.patch("https://httpbin.org/patch")
print(resposta.status_code)