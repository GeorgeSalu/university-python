"""
crie uma lista com numeros de 1 a 10
percorra a lista com um loop
quando encontrar o elemento 4 remova-o
exiba a nova list por print
"""
lista = []

i = 0
while i < 10:
    lista.append(i)
    i += 1

print(lista)

j = 0
while j < len(lista):
    if lista[j] == 4:
        del lista[j]
    j = j + 1

print(lista)