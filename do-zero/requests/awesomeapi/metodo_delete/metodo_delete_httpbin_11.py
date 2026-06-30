import requests

# Utilizando Sessão para Persistência
sessao = requests.Session()
sessao.headers.update({"X-App-Id": "XYZ"})
resposta = sessao.delete("https://httpbin.org/delete")
print(resposta.status_code)