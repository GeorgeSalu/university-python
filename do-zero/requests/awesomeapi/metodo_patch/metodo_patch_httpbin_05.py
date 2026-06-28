import requests

# Enviando Parâmetros de Query (URL)
parametros = {"id": "123"}
resposta = requests.patch("https://httpbin.org/patch", params=parametros)
print(resposta.url)