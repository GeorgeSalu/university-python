numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 0
while i < len(numeros):
    if numeros[i] == 6:
        print(f"Numero 6 encontrado no indice {i}")
        break
    i = i + 1