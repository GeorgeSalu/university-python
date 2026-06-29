import requests

resposta = requests.delete("https://httpbin.org/delete", auth=("usuario", "senha"))
print(resposta.json())
print(resposta.status_code)