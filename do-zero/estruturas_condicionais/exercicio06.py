# Exercício 6
# Uma empresa concedeu um bonus de 20% para todos os seus funcionaios com, mas de 5 anos de empresa.
# Ainda, funcionários com mais de 10 anos de empresa tem direito a uma bonificação de 30%.
# Todos os outros que não se enquadram nesta categoria receberam uma bonificação de 10%, somente.
# Escreva um algoritmo que leia o salário do funcionário e o seu tempo de empresa,
# e apresente a bonificação de cada funcionário na tela

salario = float(input("Qual o seu salário ? : "))
ano_admissao = int(input("Qual o ano de admissão ? : "))
ano_atual = int(input("Em que ano estamos ? : "))

tempo = ano_atual - ano_admissao
if tempo > 10:
    bonus = salario * 0.3
else:
    if tempo > 5:
        bonus = salario * 0.1
    else:
        bonus = salario * 0.1

print(f"voce tem {tempo} anos dentro da empresa")
print(f"seu salário é de {salario:.2f} reais")
print(f"E sua bonificação é de {bonus} reais")
print(f"Salário final: {salario + bonus}")