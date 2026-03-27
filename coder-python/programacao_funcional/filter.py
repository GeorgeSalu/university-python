#!/usr/local/bin/python3
pessoas = [
    {'nome': 'pedro', 'idade': 11},
    {'nome': 'mariana', 'idade': 18},
    {'nome': 'arthur', 'idade': 26},
    {'nome': 'rebeca', 'idade': 6},
    {'nome': 'tiago', 'idade': 19},
    {'nome': 'gabriela', 'idade': 17},
]

menores = filter(lambda p: p['idade'] < 18, pessoas)
print(list(menores))

# desafio: retornar apenas as pessoas que tem nome maior que 6 caracteres
nomes_grandes = filter(lambda p: len(p['nome']) >= 7, pessoas)
print(tuple(nomes_grandes))