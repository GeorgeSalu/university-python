# Exercício 3
# crie um programa que calcule a tabuada de um número escolhido pelo usuario
# imprima na tela a tabuada deste numero de 1 a 10

num = int(input("Digite um numero para calcular sua tabuada: "))

print(f"Tabuada do numero {num} ")
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i = i + 1