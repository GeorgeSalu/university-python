# Exercício 05
# Converter String JSON em Objeto Python (loads)
# O método loads (string load) converte uma string no formato JSON para um dicionário ou lista no Python

import json

# String no formato JSON (aspas duplas são obrigatórias no JSON)
string_json = '{"nome": "Ana", "idade": 28, "ativo": true}'

# Convertendo para dicionário Python
dados_python = json.loads(string_json)

print(dados_python["nome"])  # Saída: Ana
print(type(dados_python))