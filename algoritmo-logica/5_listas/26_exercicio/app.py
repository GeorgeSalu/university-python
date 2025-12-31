"""
crie um programa que verifique o menor valore de uma lista
"""
lista = [10,20,50,35,-14]

menor_valor = lista[0]
for i in lista:
    if i < menor_valor:
        menor_valor = i

print("o menor valor é o %d" % menor_valor)