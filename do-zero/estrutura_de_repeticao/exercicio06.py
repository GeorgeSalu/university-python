# Exercício 6
# Escreva um algoritmo que obtenha do usuario um valor inicial e um valor final
# para este intervalo especificado pelo usuario, calcule e mostre na tela:
#! A quantidade de números inteiros e positivos
#! A quantidade de números pares
# A quantidade de números impares
#! A respetiva média de cada um dos itens anteriores

qtd_positivo = 0
qtd_par = 0
qtd_impar = 0
soma_positivo = 0
soma_par = 0
soma_impar = 0

inicial = int(input("Insira um valor inicial: "))
final = int(input("Insira um valor final: "))

i = inicial
if inicial < final:
    while i <= final:
        if i > 0:
            qtd_positivo = qtd_positivo + 1
            soma_positivo = soma_positivo + i
        if i % 2 == 0:
            qtd_par = qtd_par + 1
            soma_par = soma_par + i
        else:
            qtd_impar = qtd_impar + 1
            soma_impar = soma_impar + i
        i = i + 1

    media_positivo = soma_positivo / qtd_positivo
    media_par = soma_par / qtd_par
    media_impar = soma_impar / qtd_impar
    print(f"Quantidade de valores positivos: {qtd_positivo}")
    print(f"Quantidade de valores pares: {qtd_par}")
    print(f"Quantidade de valores impar: {qtd_impar}")
    print(f"Media de valores positivos: {media_positivo}")
    print(f"Media de valores pares: {media_par}")
    print(f"Media de valores impar: {media_impar}")
else:
    print("voce digitou um valor inicial maior que o final")