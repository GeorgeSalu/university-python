# Verificar o status da requisição antes de ler o JSON
# Evita que erros de servidor ou páginas não encontradas gerem erros de decodificação.
import requests

response = requests.get("https://github.com")

if response.status_code == 200:
    dados = response.json()
    print(f"Nome: {dados['name']}")
else:
    print("Falha na requisição.")