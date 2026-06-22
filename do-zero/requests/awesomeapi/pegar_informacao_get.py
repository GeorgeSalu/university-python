import requests

# Faz a requisição para a URL
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

# Imprime o código de status (ex: 200 para sucesso)
print(requisicao.status_code)