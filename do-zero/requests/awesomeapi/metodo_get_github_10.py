# Verificando Código de Resposta e Texto
# Captura a resposta HTTP em formato de string/texto simples.
import requests

resposta = requests.get('https://api.github.com')

if resposta.ok:  # Equivalente a resposta.status_code < 400
    print(resposta.text[:100])  # Imprime os primeiros 100 caracteres