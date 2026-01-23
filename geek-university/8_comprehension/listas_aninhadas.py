"""
Listas Aninhadas

- Algumas linguagens de programação (c/java) possuem uma estrutura de dados chamados de arrays:
    - Unidimensionais (arrays/vetores)
    - Multidimensionais (matrizes)

Em Python nos temos as listas
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
"""
# exemplos
listas = [[1,2,3],[4,5,6],[7,8,9]]
print(listas)
print(type(listas))

# como fazemos para acessar os dados ?
print(listas[0][1]) # 2
print(listas[2][1]) # 8

# iterando com loops numa lista aninhada
for lista in listas:
    for num in lista:
        print(num)


# list comprehension
[[print(valor) for valor in lista] for lista in listas]

# outros exemplos
# gerando matrix 3x3
tabuleiro = [[numero for numero in range(1,4)] for valor in range(1,4)]
print(tabuleiro)

# gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else '0' for numero in range(1,4)] for valor in range(1,4)]
print(velha)