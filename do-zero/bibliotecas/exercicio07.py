# Exercício 07
# Escrever arquivo JSON
# O método dump permite salvar um objeto Python diretamente em um arquivo no formato JSON

import json

dados_para_salvar = {
    "empresa": "Tech Solutions",
    "funcionarios": 15
}

# Gravando os dados em um arquivo
with open('saida.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados_para_salvar, arquivo, indent=4)