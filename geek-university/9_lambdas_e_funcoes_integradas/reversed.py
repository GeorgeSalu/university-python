"""
Reversed

obs: não confunda com a função reverse() que estudamos nas listas
a função reverse() so funciona em listas
já a função reversed() funciona com qualquer iteravel
a sua função é inverter o iteravel
a função reversed() retorna um iteravel chamado list_reverseiterator
"""
# exemplos
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = reversed(lista)
print(res)
print(type(res))

# podemos converter o elemento retornado para uma lista, tupla ou conjunto
# lista
print(list(reversed(lista)))

# tupla
print(tuple(reversed(lista)))

# conjunto
print(set(reversed(lista)))