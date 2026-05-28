# Exercício 2
# Escreva um programa em python que encontre o maior valor dentro de uma lista e imprima-o na tela

x = [2,3,5,6,7,8,4,2,40]

maior = x[0]
for numero in x:
    if numero > maior:
        maior = numero

print(f"o maior valor é {maior}")