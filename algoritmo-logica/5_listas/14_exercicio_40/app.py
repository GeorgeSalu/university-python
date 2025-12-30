"""
crie uma lista com 5 elementos de forma dinamica
ou seja, cada elemento deve ser inserido pelo usuario
imprima na tela a lista populada de elementos
"""
l = []

i = 0
while i < 5:
    el = input("Digite um elemento: ")
    l.append(el)
    i += 1

print(l)