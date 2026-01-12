"""
3. Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.
"""
valor1: int = int(input("informe o primeiro valor: "))
valor2: int = int(input("informe o segundo valor: "))
valor3: int = int(input("informe o terceiro valor: "))

soma : int = (valor1 * valor1) + (valor2 * valor2) + (valor3 * valor3)

print(f"a soma dos quadrados dos valores {valor1} e {valor2} e {valor3} e {soma}")