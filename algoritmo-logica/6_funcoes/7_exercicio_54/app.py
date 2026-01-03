"""
escreva uma funcao que recebe uma lista de numeros
calcule a media dos numeros da lista
"""
def calcl_media(lista):
    media = 0
    soma = 0
    for n in lista:
        soma += n

    media = soma / len(lista)

    return media

notas = [9,8,7]
media_provas = calcl_media(notas)
print(media_provas)