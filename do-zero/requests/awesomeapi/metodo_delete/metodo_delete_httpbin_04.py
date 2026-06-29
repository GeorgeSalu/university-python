import requests

# Enviando Parâmetros (Params)
# Adiciona chaves de autenticação ou filtros na URL junto com os dados modificados.
url = "https://httpbin.org/delete"
meus_params = {"id_usuario": 105}

resposta = requests.delete(url, params=meus_params)

print("Status Code:", resposta.status_code)
print("Dados recebidos pelo servidor:", resposta.json())