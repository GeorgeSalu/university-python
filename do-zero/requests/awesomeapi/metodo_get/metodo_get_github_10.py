import requests

# verificando status de resposta
# Se o código de status estiver entre 200 e 400, retornará True
resposta = requests.get('https://api.github.com')

if resposta.ok:  # Equivalente a resposta.status_code < 400
    print(resposta.text[:100])  # Imprime os primeiros 100 caracteres