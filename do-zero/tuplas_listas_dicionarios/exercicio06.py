# Exercicio 5
# escreva um algoritmo que leia o nome, altura e peso de pessoas e armazene as informações numa lista
# o programa deve ir cadastrando um número indeterminado de dados e armazenar dentro da lista também o
# IMC da pessoa. Ao final do programa, imprima a lista completa e também
# o total de cadastros
# a pessoa com maior IMC
# a pessoa com menor IMC
# o cálculo do IMC deve ser realizado empregando uma função lambda e é dado como : IMC = peso / (altura^2)
# onde a massa é dado em quilograma e a altura em metros

pessoas = []
imc = lambda peso, altura: peso / (altura * 2)

while True:
    nome = input("Nome")
    altura = float(input("Altura"))
    peso = float(input("Peso"))
    x = imc(peso, altura)

    res = input("Quer continuar? [S/N]")
    if res in 'Nn':
        break

print("cadastros ", pessoas)
print("Total de cadastros : ", len(pessoas))

