# Exercício 1
# Escreva uma rotina que crie um laço de repetição que faz uma contagem
# e imprime esta contagem na tela em uma so linha
# Porem, como parametro, a função deve receber o valor inicial da contagem, o final, e o passo de iteração
# deixe os parâmetros inicial e de passo como opcionais
# você pode fazer o laço com for ou while

def contador(fim, inicio=0,passo=1):
    for i in range(inicio,fim+1, passo):
        print(f"{i}", end=" ")
    print("\n")

contador(20,10,2)
contador(12)