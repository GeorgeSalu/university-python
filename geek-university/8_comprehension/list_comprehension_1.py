"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro intravel

# sintaxe da list comprehension
[ dado for dado in iteravel ]
"""
# exemplo
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

res = [numero * 10 for numero in numeros]
print(res)

"""
Para entender melhor o que esta acontecendo devemos dividir a expressão em duas partes
- a primeira parte: for numero in numeros
- a segunda parte: numero * 10
"""

res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)

# list comprehension vs loop
# loop
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
numeros_dobrados = []
for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# list comprehension
print([numero * 2 for numero in numeros])