# Exercício 3
# Um aluno, para passar de ano,precisa estar aprovado em todas as materias que ele esta cursando
# assuma que a média para aprovação é a partir de 7, e que o aluno cursa 3 materias, somente
# escreva um algoritmo que leia a nota final do aluno em casa materia, e informe na tela se ele passou de ano ou não

m1 = float(input("Qual a primeira nota ? : "))
m2 = float(input("Qual a segunda nota ? : "))
m3 = float(input("Qual a terceira nota ? : "))

if (m1 >= 7) and (m2 >= 7) and (m3 >= 7):
    print("Aprovado")
else:
    print("Reprovado")