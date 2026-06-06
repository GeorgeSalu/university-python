# Lidar com Timeout (Tempo limite de espera)
# Define um tempo limite para evitar que o script trave caso a API demore a responder.
import requests

try:
    response = requests.get("https://api.github.com", timeout=5)
    dados = response.json()
    print("Sucesso!")
except requests.exceptions.Timeout:
    print("A requisição excedeu o tempo limite (Timeout).")