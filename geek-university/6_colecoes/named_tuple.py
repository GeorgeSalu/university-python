"""
Modulo Collections - Named Tuple

# Recap tupla
tupla = (1,2,3,4)
print(tupla[1])

Named Tuple -> São tuplas, diferenciadas, onde, especificamos um nome para mesma e também parametros
"""
from collections import namedtuple

# precisamos definir o nome e parametro
# forma 1 - declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# forma 2 - declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# forma 3 - declaração Named Tuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# usando
ray = cachorro(idade= 2, raca='chow-chow', nome='ray')
print(ray)

# acessando os dados
# forma 1
print(ray[0])
print(ray[1])
print(ray[2])

# forma 2
print(ray.idade)
print(ray.raca)
print(ray.nome)