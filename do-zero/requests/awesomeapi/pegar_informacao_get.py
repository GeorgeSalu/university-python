import requests

# Faz a requisição para a URL
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
# retorno da requisição statusCode
print(requisicao)
# retorno da requisição json
print(requisicao.json())