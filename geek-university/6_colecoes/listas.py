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

# podemos contar quanto elementos existem dentro da lista
print(len(lista1))

# podemos remover facilmente o ultimo elemento de uma lista
print(lista5)
lista5.pop()
print(lista5)

# podemos remover um elemento pelo indice
# obs: os elementos a direita deste indice serão deslocados para a esquerda
# obs: se não houver elemento no indice informado, teremos o erro IndexError
lista5.pop(2)
print(lista5)

# podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# podemos facilmente converter uma string para uma lista
# exemplo 1
curso = "programacao pyhton - essencial"
print(curso)
curso = curso.split()
print(curso)

# convertendo uma lista em uma string
lista6 = ['programacao','em','python','essencial']
print(lista6)

# abaixo estamos falando: pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# baixo estamos falando: pega a lista6, coloca cifrao entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

# interando sobre listas
# utilizando for
soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# utilizando while
carrinho = []
produto = ''

while produto != 'sair':
    print("adicione um produto na lista ou digite 'sair' para sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


# utilizando variaveis em listas
numeros = [1,2,3,4,5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1,num2,num3,num4,num5]
print(numeros)

# soma, valor maximo, valor minimo e tamanho
lista = [1,2,3,4,5]

print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

# transformando listas em tuplas
lista = [1,2,3,4,5]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# desempacotamento de listas
lista = [1,2,3]

num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)


# copiando uma lista para outra (shallow copy e deep copy)
# forma 1
lista = [1,2,3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(lista)
print(nova)

# veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas
# ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra, isso em python
# e chamado de deep copy (copia profunda)

# forma 2 shallow copy
lista = [1,2,3]
print(lista)

nova = lista
print(nova)

nova.append(4)
print(lista)
print(nova)

# veja que utilizamos a cópia via atribuição e copiamos os dados da lista para uma nova lista , ms
# após realizar uma modificação em uma das listas,essa modificação refletiu-se em ambas as litas
# isso em python é chamado de shallow copy