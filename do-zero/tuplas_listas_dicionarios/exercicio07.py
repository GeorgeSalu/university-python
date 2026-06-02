# Exercicio 7
# Escreva um programa que leia o nome de um aluno e tres notas
# armazene num dicionário o nome e a média aritmetica da nota
# ainda, armazene no dicionário a situação do aluno
#        media >= 7, aprovado
#        media < 7 e >= 5 em exame
#        media < 5, reprovado
# apresente tudo na tela ao final do programa num formato organizado

aluno = dict()
aluno['nome'] = input("Qual o nome do aluno : ")
n1 = float(input("Qual a primeira nota do aluno : "))
n2 = float(input("Qual a segunda nota do aluno : "))
n3 = float(input("Qual a terceira nota do aluno : "))
aluno['media'] = (n1 + n2 + n3) / 3

if aluno['media'] >= 7:
    aluno['status'] = 'A'
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['status'] = 'E'
else:
    aluno['status'] = 'R'

for chave, valor in aluno.items():
    print(f"{chave} = {valor}")