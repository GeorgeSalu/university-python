import requests

# Verificando o Status Code
# Gera uma exceção automática caso o código retornado pelo servidor seja de erro (4xx ou 5xx).
response = requests.post('https://httpbin.org/post')
response.raise_for_status()