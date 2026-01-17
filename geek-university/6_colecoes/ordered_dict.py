"""
Modulo Collections: Ordered Dict

# num dicionário a ordem de inserção dos elementos não e garantida
dicionario = {'a': 1, 'b': 2, 'c': 3}
print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave: {chave}, valor: {valor}')

OrderedDict -> É um dicionario que nos garante a ordem de inserção dos elementos
"""
# fazendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave: {chave}, valor: {valor}')