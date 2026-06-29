import requests

# Verificando o Tempo de Resposta (Timeout)
resposta = requests.delete("https://httpbin.org/delete", timeout=2.5)
print(resposta.elapsed.total_seconds())