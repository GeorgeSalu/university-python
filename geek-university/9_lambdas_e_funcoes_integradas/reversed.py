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

# obs: em conjuntos não definimos a ordem dos elementos
# conjunto (set)
print(set(reversed(lista)))

# podemos iterar sobre o reversed()
for letra in reversed('geek university'):
    print(letra, end='')

print()
# podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('geek university'))))

# já vimos como fazer isso, mas facil com o slice de strings
print('geek university'[::-1])

# podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)
    