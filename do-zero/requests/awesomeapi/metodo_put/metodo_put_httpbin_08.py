import requests

requisicao = requests.Request(
    "PUT", "https://httpbin.org/put", json={"teste": "debug"}
)
preparada = requisicao.prepare()
print("URL:", preparada.url)
print("Corpo:", preparada.body)