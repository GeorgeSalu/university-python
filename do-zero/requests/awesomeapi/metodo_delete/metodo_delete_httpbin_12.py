import requests

# Desativando a Verificação SSL
resposta = requests.delete("https://httpbin.org/delete", verify=False)
print(resposta.status_code)