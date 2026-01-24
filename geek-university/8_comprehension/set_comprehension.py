"""
Set Comprehension

lista = [1,2,3,4,5,6]
Set = {1,2,3,4,5,6}
"""
# exemplos
numeros = {num for num in range(1,7)}
print(numeros)

# outro exemplo
numeros = {x ** 2 for x in range(10)}
print(numeros)

# desafio: faça uma alteração na estrutura acima para gerar um dicionario ao inves de set
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# exemplo 3
letras = {letra for letra in 'geek university'}
print(letras)