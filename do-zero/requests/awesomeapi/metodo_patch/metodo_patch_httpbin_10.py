import requests

# Desativando a Verificação SSL
resposta = requests.patch("https://httpbin.org/patch", verify=False)
print(resposta.status_code)