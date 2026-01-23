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
# qualquer número par modulo de 2 é 0 e 0 em python é False, not False = True
pares = [numero for numero in numeros if not numero % 2]

# qualquer número impar modulo de 2 é 1 e 1 em python e True
impares = [numero for numero in numeros if numero % 2]
print(pares)
print(impares)

# 2
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)