import requests

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
# retorno da requesicao statusCode
print(requisicao)
# retorno da requisicao json
print(requisicao.json())