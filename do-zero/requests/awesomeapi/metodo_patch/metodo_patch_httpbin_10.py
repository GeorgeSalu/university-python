import requests

# Desativando a Verificação SSL
resposta = requests.patch("https://httpbin.org", verify=False)
print(resposta.status_code)