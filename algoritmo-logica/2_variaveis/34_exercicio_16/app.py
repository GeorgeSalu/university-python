"""
Crie um programa que recebe um valo como salario
e outro como porcentagem de aumento
exiba o valor tatal apos o aumento no interpretador
"""
salario = float(input("digite o salario : "))
aumento = float(input("Digite o aumento : "))

print(salario)
print(aumento)

novo_salario = salario + (salario * aumento/100)
print("o novo salario é de %.2f" % novo_salario)