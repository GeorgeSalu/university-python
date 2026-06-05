# Exercício 04
# json (Manipulação de Dados)
# Muito usada para ler, escrever e converter dados estruturados, crucial para trabalhar com APIs.

import json

# Converter dicionário Python para string JSON
dados = {"nome": "Ana", "idade": 25}
json_string = json.dumps(dados)
print(json_string)