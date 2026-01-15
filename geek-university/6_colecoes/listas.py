"""
listas
listas em python funcionam como vetores/matrizes (arrays) em outroas linguagens, com a diferença
de serem dinamico e também podermos ter qualquer tipo de dado

linguagens c/java: arrays
 - possuem tamanho e tipo de dado fixo;
 ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
 sera sempre do tipo inteiro e podera sempre ter sempre no maximo 5 valores

 Já em python
 - dinamico: não possuem tamanho fixo; ou seja, podemos criar a lista e simplesmente ir adicionando elementos
 - Qualquer tipo de dado: não possuem tipo de dado fixo: ou seja, podemos colocar qualquer tipo de dado

 as listas em python são representadas por colchetes: []
"""
type([])
lista1 = [1,2,3,4,5,4,3,22,11]
lista2 = ['g','e','e','k',' ','u','n','i','v','e','r','s','i','t','y']
lista3 = []
lista4 = list(range(11))
lista5 = list('geek university')

# podemos checar se determinado valor esta contido na lista
num = 7
if num in lista4:
    print(f"encontrei o numero {num}")
else:
    print(f"nao encontrei o numero {num}")

# podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# podemos facilmente contar o numero de ocorrencia de uma valor em uma lista
print(lista1.count(1))
print(lista1.count('e'))

# adicionar elementos em listas
# para adicionar elementos em listas utilizamos a função append
print(lista1)
lista1.append(42)
print(lista1)

# adicionando mas de um elemento
lista1.extend([123,44,67]) # coloca cada elemento da lista como valor adicional a lista
print(lista1)

# podemos inserir um novo elemento na lista informando a posicao do indice
lista1.insert(2,"novo valor")
print(lista1)

# podemos facilmente juntar duas listas
lista6 = lista1 + lista2
print(lista6)

# lista reversa
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# lista reversa forma 2
print(lista1[::-1])
print(lista2[::-1])

# copiar lista
lista6 = lista2.copy()
print(lista6)