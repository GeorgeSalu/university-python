# Exercício 5
# Escreva um algoritmo que leia dois valores e imprima na tela o resultado da multiplicacao ed ambos
# Porém, para calcular a multiplicação, utilize somente operações de soma e subtração
# Lembrando que uma multiplicação pode ser considerada como uma somatorio sucessivo
# utilize esta logica para construir o seu algoritmo.

x = int(input("Digite um valor: "))
y = int(input("Digite um segundo valor: "))

multi = 0
i = 1
while i <= x:
    multi = multi + y
    i = i + 1

print(f"Resultado da multiplicacao: {x}x{y} = {multi}")