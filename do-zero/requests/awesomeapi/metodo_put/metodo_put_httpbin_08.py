import requests

# Inspecionando a requisição enviada
# Visualiza exatamente o que o requests enviou antes de receber a resposta do servidor.
requisicao = requests.Request(
    "PUT", "https://httpbin.org/put", json={"teste": "debug"}
)
preparada = requisicao.prepare()
print("URL:", preparada.url)
print("Corpo:", preparada.body)