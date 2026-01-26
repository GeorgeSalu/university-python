"""
Generators

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