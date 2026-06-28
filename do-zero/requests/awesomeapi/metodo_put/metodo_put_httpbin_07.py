import requests

# Desabilitando a verificação SSL
# Útil para desenvolvimento local com certificados auto-assinados (em produção, mantenha como True).
resposta = requests.put(
    "https://httpbin.org/put", json={" ssl": "ignorado"}, verify=False
)
print(resposta.status_code)