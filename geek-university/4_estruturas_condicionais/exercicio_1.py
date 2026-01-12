"""
1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
"""
numero1: int = int(input("informe o primeiro numero: "))
numero2: int = int(input("informe o segundo numero: "))

if numero1 > numero2:
    print(f"o numero {numero1} eh maior que o numero {numero2}")
elif numero1 == numero2:
    print(f"os numeros {numero1} e {numero2} são iguais")
else:
    print(f"o numero {numero2} eh maior que {numero1}")