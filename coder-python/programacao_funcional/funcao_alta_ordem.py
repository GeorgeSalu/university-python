#!/usr/local/bin/python3
from funcao_primeira_classe import dobro, quadrado

def processar(titulo, lista, funcao):
    print(f'Procesando: {titulo}')
    for i in lista:
        print(i, '=>', funcao(i))


if __name__ == '__main__':
    processar('dobros de 1 a 10', range(1,10), dobro)
    processar('quadrado de 1 a 10', range(1,10), quadrado)