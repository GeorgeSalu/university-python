# Exercício 2
# Escreva uma rotina que recebe tres valores como parametro e coloque-os em ordem crescente.
# Ou seja, do menor ao maior
# imprima na tela os tres valores

def maior3(v1 = 0, v2 = 0, v3 = 0):
    if v1 and v2 and v3:
        if (v1 > v2) and (v1 > v3):
            if v2 > v3:
                print(f"Ordem crescente: {v3}, {v2}, {v1}")
            else:
                print(f"Ordem crescente: {v2}, {v3}, {v1}")
        elif (v2 > v1) and (v2 > v3):
            if v1 > v3:
                print(f"Ordem crescente: {v3}, {v1}, {v2}")
            else:
                print(f"Ordem crescente: {v1}, {v3}, {v2}")
        elif (v3 > v1) and (v3 > v2):
            if v1 > v2:
                print(f"Ordem crescente: {v3}, {v2}, {v1}")
            else:
                print(f"Ordem crescente: {v2}, {v3}, {v1}")


# programa principal
x = int(input("Informe o primeiro valor: "))
y = int(input("Informe o segundo valor: "))
z = int(input("Informe o terceiro valor: "))
maior3(x,y,z)