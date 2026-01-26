"""
Generator Expression

Em aul anteriores nos estudamos
- list comprehension
- dict comprehension
- set comprehension

Não vimos:
- Tuple comprehension... por que elas se chamam Generators

nomes = ['carlos','camila','carla','cassiano','cristiana','vanessa']

print(any(nome[0] == 'c' for nome in nomes))
"""
# poderiamos ter feitos utilizando generators

nomes = ['carlos','camila','carla','cassiano','cristiana','vanessa']
print(any(nome[0] == 'c' for nome in nomes))

# list comprehensions
res = [nome[0] == 'c' for nome in nomes]
print(type(res))
print(res)

# generator
res = (nome[0] == 'c' for nome in nomes)
print(type(res))
print(res)

# qual é a utilizade de getsizeof() ? -> retorna a quantidade de bytes em memória do elemento passado como parametro
from sys import getsizeof

# mostra quantos bytes a string 'geek' esta ocupando em memória, quanto maior a string, mais espaco ocupa
print(getsizeof('geek'))
print(getsizeof('university'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(929384433))
print(getsizeof(True))

# gerando uma lista de números com list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# gerando uma lista de números com set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# gerando uma lista de números com dict comprehension
dict_comp = getsizeof({x:x * 10 for x in range(1000)})

# gerando uma lista de números com generators
gen = getsizeof(x * 10 for x in range(1000))

print(f'para fazer a mesma tarefa gastamos em memoria : ')
print(f'list comprehension: {list_comp}')
print(f'set comprehension: {set_comp}')
print(f'dict comprehension: {dict_comp}')
print(f'generator comprehension: {gen}')

# eu posso iterar no generator expression

gen = (x * 10 for x in range(1000))
print(type(gen))
print(gen)

for num in gen:
    print(num)