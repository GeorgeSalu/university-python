"""
loop for
"""
nome = "geek university"
lista = [1, 2, 3, 4, 5]
numeros = range(1,10)

# interando em uma string
for letra in nome:
    print(letra)

# interando em uma lista
for numero in lista:
    print(numero)

# interando em um range
for numero in numeros:
    print(numero)

print("********************************************")
# enumerated
for indice, valor in enumerate(nome):
    print(indice, valor)

for indice, letra in enumerate(nome):
    print(letra)

# quando não precisamos de uma valor, podemos descarta-lo utilizando um underline (_)
for _, letra in enumerate(nome):
    print(letra)

print("********************************************")