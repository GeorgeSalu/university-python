# Enviar cabeçalhos (Headers) JSON personalizados
# Informações essenciais para APIs que exigem autenticação ou aceitam apenas requisições JSON.
import requests

headers = {
    "Authorization": "Bearer SEU_TOKEN_AQUI",
    "Content-Type": "application/json"
}
response = requests.get("https://github.com", headers=headers)

print(response.json())