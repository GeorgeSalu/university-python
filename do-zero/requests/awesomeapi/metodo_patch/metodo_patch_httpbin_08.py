import requests

# Lançando Exceção para Erros HTTP (4xx ou 5xx)
resposta = requests.patch("https://httpbin.org")
resposta.raise_for_status()