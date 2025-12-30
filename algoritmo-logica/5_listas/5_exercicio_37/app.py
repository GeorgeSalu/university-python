"""
crie uma lista com 5 valores zerados
faça um loop para percorrer a lista e preencher os valores zerados
os valores devem ser inseridos pelo usuario
imprima o resultado final com print
"""
lista = [0,0,0,0,0]

print(lista)

i = 0
while i < 5:
    numero = int(input("Digite um numero %d : "%i))
    lista[i] = numero
    i += 1

print(lista)
