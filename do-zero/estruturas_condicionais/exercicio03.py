# Exercício 3
# Uma empresa concedeu um bonus de 20% para todos os seus funcionaios com, mas de 5anos de empresa.
# Todos os outros que não se enquadram nesta categoria receberam uma bonificação de 10%, somente.
# Escreva um algoritmo que leia o salário do funcionario e o seu tempo de empresa,
# e apresente a bonificação de cada funcionario na tela

salario = float(input("Qual o seu salario ? : "))
ano_admissao = int(input("Qual o ano de nascimento ? : "))
ano_atual = int(input("Em que ano estamos ? : "))

tempo = ano_atual - ano_admissao
if (tempo > 5):
    bonus = salario * 0.2
else:
    bonus = salario * 0.1

print(f"voce tem {tempo} anos dentro da empresa")
print(f"seu salario é de {salario:.2f} reais")
print(f"E sua bonificacao é de {bonus} reais")
print(f"Salario final: {salario + bonus}")