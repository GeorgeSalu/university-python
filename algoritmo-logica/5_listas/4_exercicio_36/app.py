"""
crie uma lista com 5 notas de prova de um aluno
faça um loop que calcula a media das notas
imprima o resultado final
"""
notas = [10,8,5,8,7]

print(notas)

i = 0
soma_notas = 0

while i < 5:
    soma_notas = soma_notas + notas[i]
    i = i + 1

media = soma_notas/5
print("o aluno teve a media %.1f na materia x"%media)