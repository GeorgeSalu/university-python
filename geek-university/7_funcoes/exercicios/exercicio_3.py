"""
3. Faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor.
"""

def maior(inteiro: list[int]) -> int:
    return max(inteiro)


if __name__ == '__main__':
    lista: list[int] = [2,3,4,3,60,4]
    print(f'o maior valor na lista {lista} eh {maior(lista)}')