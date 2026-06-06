# Enviar JSON usando data (Alternativa manual)
# Serializa o dicionário usando a biblioteca embutida json.dumps() (comum em APIs mais antigas)
import requests
import json

payload = {"status": "ativo"}
headers = {"Content-Type": "application/json"}

response = requests.post(
    "https://httpbin.org",
    data=json.dumps(payload),
    headers=headers
)
print(response.json())