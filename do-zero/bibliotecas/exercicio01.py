# Exercício 01
# Desenvolva um algoritmo que solicite ao usuário uma quantidade de dias, de horas, de minutos e de segundos
# Calcule total de segundos resultantes e imprima na tela para o usuário

from datetime import timedelta

d = int(input("quantos dias ? : "))
h = int(input("quantas horas ? : "))
m = int(input("quantos minutos ? : "))
s = int(input("quantos segundos ? : "))

total = s + timedelta(minutes=m).total_seconds() + timedelta(hours=h).total_seconds() + timedelta(days=d).total_seconds()
res = f"O total de segundos calculados é de {total}"
print(res)