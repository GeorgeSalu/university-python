# Exercicio 5
# O algoritmo mais simples de se buscar um dado numa estrutura de dados é chamado de busca sequencial
# a busca sequencial é uma varredura simples do primeiro ao último elemento da estrutura, verificando
# se o dado desejado se encontra presente, escreva uma função que receba como parametro uma lista e um dado
# verifique se o dado esta presente na lista e retorne da função o seu indice, caso ele esteja presente
# caso contrario retorne -1

def buscaSequencial(lista, dado):
    x = 0
    while x < len(lista):
        if lista[x] == dado:
            return x
        x += 1
    return -1


# programa principal
teste = [6,8,7,9,0,5,3]
dado = int(input("Digite um valor para buscar : "))
res = buscaSequencial(teste, dado)
if res >= 0:
    print(f"posicao onde o {dado} foi encontrado : {res + 1}")
else:
    print(f"dado nao foi encontrado")