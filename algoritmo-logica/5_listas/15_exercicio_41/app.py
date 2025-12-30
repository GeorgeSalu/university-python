"""
crie duas varivaies de listas
crie uma terceira lista com todos os elementos das duas listas anteriores
"""
lista_a = [1,2,3,4,5]
lista_b = [4,5,6,7,8]

print(lista_a)
print(lista_b)

lista_c = []

i = 0
while i < len(lista_a):
    lista_c.append(lista_a[i])
    i += 1

j = 0
while j < len(lista_b):
    lista_c.append(lista_b[j])
    j += 1

print(lista_c)