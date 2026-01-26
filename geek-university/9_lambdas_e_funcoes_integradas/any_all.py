"""
Any e All

all() -> retorna True se todos os elementos do iteravel são verdadeiros ou ainda se o iteravel está vazio
any() -> retorna True se qualquer elemento do iteravel for verdadeiro, se o iteravel etiver vazio, retorna False
"""
# exemplo all
print(all([0,1,2,3,4])) # todos os números são verdadeiros ? False
print(all([1,2,3,4])) # todos os números são verdadeiros ? True
print(all([])) # todos os números são verdadeiros ? True
print(all([1,2,3,4])) # todos os números são verdadeiros ? True
print(all({1, 2, 3, 4})) # todos os números são verdadeiros ? True
print(all('geek')) # todos os números são verdadeiros ? True

nomes = ['carlos','camila','carla','cassiano','cristina']
print(all(nome[0] == 'c' for nome in nomes))

# obs: um iteravel vazio convertido em boolean é False m o all() entende como True

# exemplo any
print(any([0,1,2,3,4])) # True
print(any([0, False, {}, (), []]))