# Exercício 4
# desenvolva um algoritmo que converta uma temperatura em Celsius (C) para Faherenheit (F).
# a equação de conversão é
# 9 x Celsius, tudo dividido por 5 e somado com 32

c = float(input("Digite a temperatura em Celsius: "))
f = (9 * c) / 5 + 32

print(f"Celsius: {c} Fahrenheit: {f}")