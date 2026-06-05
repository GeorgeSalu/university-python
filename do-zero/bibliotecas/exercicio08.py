# Exercício 08
# Ler arquivo JSON (load)
# O método load é usado para ler um arquivo .json diretamente e convertê-lo para estruturas Python

import json

# Lendo dados de um arquivo
with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dados_carregados = json.load(arquivo)

print(dados_carregados)