"""
escreva uma funcao que recebe uma lista de numeros
a funcao deve retornar apenas os numeros pares da lista
"""

def retorna_lista_par(l):
    nova_lista = []

    for numero in l:
        if numero % 2 == 0:
            nova_lista.append(numero)

    return nova_lista

lista = [1,2,3,4,5,6,7,8]
lista_pal = retorna_lista_par(lista)
print(lista_pal)