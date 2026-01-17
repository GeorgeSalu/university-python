"""
Modulo Collections - counter
Collections -> Heigh-performance Container Datetypes

Counter -> Recebe um interavel como parametro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parametro e como valor a quantidade
de ocorrencias desse elemento
"""
# realizando o import
from collections import Counter

# podemos utilizar qualquer iteravel, aqui usamos uma lista
lista = [1,1,2,22,2,3,4,5,6,7,8,9,8,8,89,10,10,20,10]

# utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)

# Counter({8: 3, 10: 3, 1: 2, 2: 2, 22: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 89: 1, 20: 1})
# veja que para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrencias