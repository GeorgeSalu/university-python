# Exercício 06
# Converter Objeto Python para String JSON (dumps)
# O método dumps (string dump) faz o processo inverso, serializando um objeto Python (como um dicionário) em uma string de texto JSON

import json

dados_python = {
    "nome": "Carlos",
    "linguagens": ["Python", "JavaScript"],
    "online": True
}

# Convertendo para string JSON (com formatação legível)
string_json = json.dumps(dados_python, indent=4, ensure_ascii=False)

print(string_json)