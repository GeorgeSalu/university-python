import requests

# Lançando Exceção para Erros HTTP (4xx ou 5xx)
resposta = requests.delete("https://httpbin.org/delete")
resposta.raise_for_status()