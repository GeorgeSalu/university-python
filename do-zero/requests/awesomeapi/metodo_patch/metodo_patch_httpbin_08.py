import requests

# Lançando Exceção para Erros HTTP (4xx ou 5xx)
resposta = requests.patch("https://httpbin.org/patch")
resposta.raise_for_status()