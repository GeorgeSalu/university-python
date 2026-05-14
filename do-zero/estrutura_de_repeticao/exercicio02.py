# Exercício 2
# suponhamos que desejamos exibir uma série de números na tela
# onde os limites de início e fim dessa sequência são determinados pelo usuário que executa o programa
# crie um algoritmo que leia os valores de início e de fim e imprima na tela o intervalo de números
# pares correspondentes

inicial = int(input("digite o valor inicial da contagem ? "))
final = int(input("digite o valor final da contagem ? "))

i = inicial
while i <= final:
    if i % 2 == 0:
        print(i)
    i = i + 1