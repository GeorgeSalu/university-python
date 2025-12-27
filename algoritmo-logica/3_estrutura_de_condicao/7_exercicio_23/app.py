"""
crie um programa com a variavel salario
se for maior que 1800 imprima uma mensagem de que é necessario pagar imposto de renda
se não imprima uma mensagem que não precisa parr IR
"""
salario = float(input("Qual o seu salario? "))

if salario > 1800:
    print("voce precisa pagar imposto de renda")
else:
    print("voce nao precisa pagar imposto de salario")