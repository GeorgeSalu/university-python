import requests

# Faz a requisição para a URL
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

# Mostra a URL final
print(requisicao.url)

# Imprime o código de status (ex: 200 para sucesso)
print(requisicao.status_code)

# Converte o retorno diretamente para um dicionário Python (se a API retornar JSON)
dados_json = requisicao.json()
print(dados_json)

# Verificando Cabeçalhos de Resposta
print(requisicao.headers["Content-Type"])
