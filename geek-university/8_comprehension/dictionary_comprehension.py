"""
Dictionary Comprehension

Pense no seguinte:
se quisermos criar uma lista fazemos
lista = [1,2,3,4]
se quisermos criar uma tupla
tupla = (1,2,3,4)
se quisermos criar um set
conjunto = {1,2,3,4,5}
se quisermos criar um dicionario
dicionario = {'a':1,'b':2,'c':3,'d':4,'e':5}

# sintaxy
{chave:valor for valor in iteravel}
"""
# exemplo 1
numeros = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
quadrado = {chave:valor **2 for chave, valor in numeros.items()}
print(quadrado)

# exemplo 2
numero = [1,2,3,4,5,6,7,8,9,10]
quadrados = {valor: valor ** 2 for valor in numero}
print(quadrados)


# exemplo 3
chaves = 'abcde'
valores = [1,2,3,4,5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# exemplo 4 - com lógica condicional
numeros = [1,2,3,4,5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)