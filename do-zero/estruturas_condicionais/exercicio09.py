# Exercício 9
# Escreva um algoritmo que leia dois valores numericos e que pergunte ao usuario qual operação ele deseja realizar:
# adição(+), subtração(-), multiplicação(*) ou divisão(/) exiba na tela o resultado da operação desejada

print("calculadora")
print("+ adição")
print("- subtracao")
print("* multiplicacao")
print("/ divisao")
print("digite outra tecla para sair")

op = input("Qual operação deseja realizar ? ")
x = int(input("digite o primeiro numero : "))
y = int(input("digite o segundo numero : "))

if op == "+":
    res = x + y
    print(f"Resultado: {x} + {y} = {res} ")
elif op == "-":
    res = x - y
    print(f"Resultado: {x} - {y} = {res} ")
elif op == "*":
    res = x * y
    print(f"Resultado: {x} * {y} = {res} ")
elif op == "/":
    res = x / y
    print(f"Resultado: {x} / {y} = {res} ")
else:
    print("Operacao invalida")