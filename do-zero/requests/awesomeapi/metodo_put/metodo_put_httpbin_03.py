import requests

# Enviando parâmetros na URL (Query Strings)
# Adiciona parâmetros para filtrar ou instruir a ação do servidor.
parametros = {"id": 42}
resposta = requests.put(
    "https://httpbin.org/put", params=parametros, data={"status": "ativo"}
)
print(resposta.url)
