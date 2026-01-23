"""
List Comprehension

Podemo-nos adicionar estruturas condicionais logicas as nossas List Comprehension
"""
# exemplo
# 1
numeros = [1,2,3,4,5,6,7,8,9]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

# refatorado
pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]
print(pares)
print(impares)