"""
Sorted

obs: não confunda, apesar do nome,com a função sort() que já estudamos em listas, o sort()
so funciona em listas.

Podemos utilizar o sorted() com qualquer iteravel

Como o proprio nome diz, sorted() serve para ordenar.

obs: o sorted() sempre retorna uma lista com os elementos do iteravel ordenados
"""
# exemplo
numeros = [1,2,102,9,4,6]
print(numeros)
print(sorted(numeros)) # ordena do menor para o maior
print(numeros)

# adionando parametros ao sorted()
numeros = [6,1,8,2]
print(numeros)
print(sorted(numeros, reverse=True)) # ordena do maior para o maior

