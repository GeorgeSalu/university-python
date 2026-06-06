# Enviar dados JSON numa requisição POST
# Utiliza o parâmetro json=... para serializar automaticamente o dicionário
import requests

payload = {"nome": "João", "cargo": "Desenvolvedor"}
response = requests.post("https://httpbin.org", json=payload)

print(response.json())