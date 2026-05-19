# Exercício 11
# escreva um algoritmo que encontre todos os números primos de 2 ate 99
# imprima todos eles na tela

print("primos de 2 ate 99")
for numero in range(2, 100, 1):
    flag = 0
    for i in range(2, numero, 1):
        if numero % i == 0:
            flag = 1
            break
    if flag == 0:
        print(numero)