# Exercício 4
# crie um programa que calcule a soma de 5 valores inteiros, cada valor a ser somado é digitado pelo usuario
# imprima a soma na tela, após a soma,calcule também a média dos valores e mostre na tela

soma = 0
i = 1
while i <= 5:
    x = int(input(f"Digite um valor {i}: "))
    soma = soma + x
    i = i + 1

print(f"Somatorio: {soma}")
media = soma / 5
print(f"Media final: {media}")