# Usar raise_for_status() para tratamento de exceções
# Lança uma exceção se a requisição retornar um código de erro HTTP (ex: 404 ou 500)
import requests

try:
    response = requests.get("https://github.com")
    response.raise_for_status()  # Levanta erro para status HTTP 4xx/5xx
    dados = response.json()
except requests.exceptions.HTTPError as err:
    print(f"Erro HTTP: {err}")