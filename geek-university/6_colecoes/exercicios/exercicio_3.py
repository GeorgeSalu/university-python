"""
3. Faça um programa que leia 10 valores, armazene-os numa lista e apresente quantos valores pares ele possui.
"""
lista: list[int] = []
contador_pares: int = 0

while len(lista) < 10:
    valor: int = int(input(f'informe o valor {len(lista)+1}/10: '))
    lista.append(valor)

    if valor % 2 == 0:
        contador_pares += 1

if contador_pares > 0:
    print(f'a lista {lista} possui {contador_pares} pares')
else:
    print(f'a lista não possui valores pares')