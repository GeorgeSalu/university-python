# Exercício 9
# crie um programa que calcule a tabuada de um número escolhido pelo usuario
# imprima na tela a tabuada deste numero de 1 a 10. Ao realizar a impressão na tela, mostre os valores formatado
# exemplo com a tabuada de 5: 1x5=5, 2x5=10, 3x5=15

num = int(input("digite um numero para calcular sua tabuada: "))
print(f"Tabuada do numero {num} ")

for i in range(1, 11, 1):
    print(f"{num} x {i} = {num * i}")