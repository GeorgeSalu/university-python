"""
Min e Max

max() -> retorn o maior valor em iterável ou o maior de dois, ou mais elementos
min() -> retorna o menor valor num iterável ou o menor de dois, ou mais elementos
"""
# exemplos max()
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(lista))

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(max(tupla))

conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(max(conjunto))

dicionario = {'a':1, 'b':2, 'c':3}
print(max(dicionario))

dicionario = {'a':1, 'b':2, 'c':3}
print(max(dicionario.values()))

print(max(4,67,54))
print(max('a','ab','abc'))
print(max('a','b','c','d'))

# exemplos min()
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(lista))

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(min(tupla))

conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(min(conjunto))

dicionario = {'a':1, 'b':2, 'c':3}
print(min(dicionario))

dicionario = {'a':1, 'b':2, 'c':3}
print(min(dicionario.values()))

print(min(4,67,54))
print(min('a','ab','abc'))
print(min('a','b','c','d'))
print(min('geek university'))

# outros exemplos
nomes = ['arya','samson','dora','tim','ollivander']
print(max(nomes))   # tim
print(min(nomes))   # arya
print(max(nomes, key=lambda nome: len(nome)))   # ollivander
print(min(nomes, key=lambda nome: len(nome)))   # tim


musicas = [
    {"titulo": "thunderstructk", "tocou": 3},
    {"titulo": "Dead skin mask", "tocou": 2},
    {"titulo": "Back in black", "tocou": 4},
    {"titulo": "too old to rock", "tocou": 32},
]

print(max(musicas, key=lambda musica: musica["tocou"]))
print(min(musicas, key=lambda musica: musica["tocou"]))

# imprima somente o título da musica mais e menos tocada
print(max(musicas, key=lambda musica: musica["tocou"])["titulo"])
print(min(musicas, key=lambda musica: musica["tocou"])['titulo'])

# como encontrar a musica mais tocada e a menos tocada sem usar max() e min() e lambda ?
max = 0
for musica in musicas:
    if musica["tocou"] > max:
        max = musica["tocou"]

for musica in musicas:
    if musica["tocou"] == max:
        print(musica["titulo"])

min = 9999
for musica in musicas:
    if musica["tocou"] < min:
        min = musica["tocou"]

for musica in musicas:
    if musica["tocou"] == min:
        print(musica["titulo"])
