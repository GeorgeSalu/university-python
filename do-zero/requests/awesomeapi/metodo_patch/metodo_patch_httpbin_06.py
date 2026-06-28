import requests

# Verificando o Tempo de Resposta (Timeout)
resposta = requests.patch("https://httpbin.org/patch", timeout=2.5)
print(resposta.elapsed.total_seconds())