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

# entendendo a diferenca entre Dict e OrderedDict
# dicionarios comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)

# OrderedDict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2)