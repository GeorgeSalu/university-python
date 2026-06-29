import requests

# Enviando Parâmetros (Params) e Cabeçalhos (Headers)
# Adiciona chaves de autenticação ou filtros na URL junto com os dados modificados.
url = "https://httpbin.org/delete"
meus_headers = {"Authorization": "Bearer SEU_TOKEN_AQUI"}
meus_params = {"id_usuario": 105}
dados_patch = {"nome": "Novo Nome"}

resposta = requests.delete(url, params=meus_params, data=dados_patch, headers=meus_headers)

print("Status Code:", resposta.status_code)
print("Dados recebidos pelo servidor:", resposta.json())
