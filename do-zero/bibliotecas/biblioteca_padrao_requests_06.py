# Parâmetros de URL (Query Strings) em formato JSON
# Passa parâmetros na URL como um dicionário Python simples.
import requests

parametros = {"q": "requests", "language": "python"}
response = requests.get("https://github.com", params=parametros)

print(f"Total de resultados: {response.json()['total_count']}")