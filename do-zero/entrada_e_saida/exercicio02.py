# exercício 2
# desenvolva m algoritmo que solicite ao usuário uma quantidade de dias,
# de horas, de minutos e de segundos
# calcule o total de segundos resultante e imprima n tela para o usuario

d = int(input("quantos dias: "))
h = int(input("quantos horas: "))
m = int(input("quantos minutos: "))
s = int(input("quantos segundos: "))

total = s + (m * 60) + (h * 60 * 60) + (d * 24 * 60 * 60)

res = f"O total de segundos calculado é de {total}"
print(res)