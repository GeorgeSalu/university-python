pessoas = [
    {'nome': 'joao', 'idade': 31},
    {'nome': 'maria', 'idade': 37},
    {'nome': 'jose', 'idade': 41},
]

menores = filter(lambda p: p['idade'] < 18, pessoas)
print(list(menores))