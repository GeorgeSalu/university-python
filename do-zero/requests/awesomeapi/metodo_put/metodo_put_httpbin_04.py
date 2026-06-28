import requests

# Configurando Cabeçalhos (Headers)
# Envia metadados sobre a requisição (como especificar autenticação ou formato de dado).
cabecalhos = {"Authorization": "Bearer meu_token_secreto", "Content-Type": "application/json"}
resposta = requests.put(
    "https://httpbin.org/put", headers=cabecalhos, json={"ativo": True}
)
print(resposta.json())
print(resposta.json()["headers"]["Authorization"])