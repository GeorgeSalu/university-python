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
# exemplo
numeros = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
quadrado = {chave:valor **2 for chave, valor in numeros.items()}
print(quadrado)