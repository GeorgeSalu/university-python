import requests

# Faz a requisição para a URL
# Requisição Simples
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

# Ler Resposta em Bytes (Para Imagens/Arquivos)
print(requisicao.content)

# .text: Retorna o conteúdo da resposta como uma string (muito usado para HTML ou texto simples)
dados_text = requisicao.text
print(dados_text)

# Verificando Cabeçalhos de Resposta
print(requisicao.headers["Content-Type"])

# Recebendo Dados em JSON
dados = requisicao.json()
print(dados["USDBRL"])
print(dados["USDBRL"].get("code"))
print(dados["USDBRL"].get("name"))
print(dados["EURBRL"])
print(dados["EURBRL"].get("code"))
print(dados["EURBRL"].get("name"))
print(dados["BTCBRL"])
print(dados["BTCBRL"].get("code"))
print(dados["BTCBRL"].get("name"))

# .cookies: acessa os cookies enviados ou definidos pelo servidor.
print(requisicao.cookies)