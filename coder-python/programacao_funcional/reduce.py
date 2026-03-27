#!/usr/local/bin/python3
from functools import reduce

pessoas = [
    {'nome': 'pedro', 'idade': 11},
    {'nome': 'mariana', 'idade': 18},
    {'nome': 'arthur', 'idade': 26},
    {'nome': 'rebeca', 'idade': 6},
    {'nome': 'tiago', 'idade': 19},
    {'nome': 'gabriela', 'idade': 17},
]

soma_idades = reduce(lambda idades, p: idades + p['idade'], pessoas, 0)
print(soma_idades)