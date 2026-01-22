"""
1. Crie um programa que tenha uma função que recebe um parâmetro inteiro e devolve o seu dobro.
"""
def dobro(numero: int) -> int:
    return numero * 2

if __name__ == '__main__':
    valor = 4
    print(f'o dobro de {valor} eh {dobro(valor)}')