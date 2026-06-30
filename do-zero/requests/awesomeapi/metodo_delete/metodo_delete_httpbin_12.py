import requests

resposta = requests.delete("https://httpbin.org/delete", verify=False)
print(resposta.status_code)