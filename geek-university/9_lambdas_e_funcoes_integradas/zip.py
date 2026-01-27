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

# obs: o zip utiliza como parametro o menor tamanho em iteravel, isso significa que se estiver
# trabalhando com iteraveis de tamanhos diferentes, ira para quando os elementos do menor iteravel acabar
lista3 = [1, 2, 3, 4, 5]

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

# podemos utilizar diferentes iteraveis com zip
tupla = 1,2,3,5
lista = [6,7,8,9,10]
dicionario = {'a': 1, 'b': 2, 'c': 3}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# lista de tuplas
dados = [(0,1), (1,2), (2,3), (3,4)]
print(list(zip(*dados)))