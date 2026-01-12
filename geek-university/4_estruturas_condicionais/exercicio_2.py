"""
2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.
"""
import math

numero: int = int(input("informe um numero inteiro: "))

if numero > 0:
    print(f"a raiz quadrada de {numero} e igual a {math.sqrt(numero)}")
else:
    print(f"o numero {numero} é invalido")