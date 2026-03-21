#!/usr/local/bin/python3
def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular


if __name__ == '__main__':
    dobro = multiplicar(2)
    triplo = multiplicar(3)
    print(dobro, triplo)
    print(f'o triplo de 3 é {triplo(3)}')
    print(f'o dobro de 7 é {dobro(7)}')