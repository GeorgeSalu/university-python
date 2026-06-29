import requests

# Enviando Parâmetros de Query (URL)
parametros = {"id": "123"}
resposta = requests.delete("https://httpbin.org/delete", params=parametros)
print(resposta.url)