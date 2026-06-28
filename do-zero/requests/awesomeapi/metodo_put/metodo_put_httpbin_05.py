import requests

try:
    resposta = requests.put("https://httpbin.org/put", json={"ok": 1}, timeout=5)
    print(resposta.status_code)
except requests.exceptions.Timeout:
    print("A requisição excedeu o tempo limite.")