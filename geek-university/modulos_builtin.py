"""
Trabalhando com modulos builtin (modulos integrados, que ja vem instalados no python)
"""
# utilizando alias (apelidos) para modulos/funções
import random as rdm

print(rdm.random())

# podemos importar todas as funções de um módulo utilizando o *
from random import *

print(random())

# importando todo o modulo
import random

print(random.random())

# utilizando alias (apelidos) para modulos/funcoes
from random import randint as rdi

print(rdi(5, 89))

# costumamos utilizar tuple para colocar multiplos imports de um mesmo modulo
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(1,100))
lista = ['geek','university','python']
shuffle(lista)
print(lista)
print(choice('university'))