import requests

# Faz a requisição para a URL
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

# Mostra a URL final
print(requisicao.url)

# Imprime o código de status (ex: 200 para sucesso)
print(requisicao.status_code)

# .raise_for_status(): Lança um erro automaticamente caso a requisição termine em falha (status 4xx ou 5xx)
print(requisicao.raise_for_status())

# Converte o retorno diretamente para um dicionário Python (se a API retornar JSON)
dados_json = requisicao.json()
print(dados_json)

# .text: Retorna o conteúdo da resposta como uma string (muito usado para HTML ou texto simples)
dados_text = requisicao.text
print(dados_text)

# Verificando Cabeçalhos de Resposta
print(requisicao.headers["Content-Type"])

# Recebendo Dados em JSON
dados = requisicao.json()
print(dados["USDBRL"])
print(dados["EURBRL"])
print(dados["BTCBRL"])

# .cookies: Acessa os cookies enviados ou definidos pelo servidor.
print(requisicao.cookies)