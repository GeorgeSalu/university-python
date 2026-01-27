"""
Zip

zip() -> cria um iteravel (Zip Object) que agrega elemento de cada um dos iteraveis passados como entrada em pares
"""
# exemplos
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

zip1 = zip(lista1, lista2)
print(zip1)
print(type(zip1))

# sempre podemos gerar uma lista, tupla ou dicionrio
print(list(zip1))

zip1 = zip(lista1, lista2)
print(tuple(zip1))

zip1 = zip(lista1, lista2)
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))