"""
crie uma lista com outras listas dentro dela
uma ideia seria: produtos com nome, cor e preço
imprima cada um dos itens da listas que estão inseridas na lista pai
"""
produtos_a = ["camisa","azul",25.44]
produtos_b = ["bermuda","marrom",125.44]
produtos_c = ["casaco", "bege", 11]

lista_produtos = [produtos_a,produtos_b,produtos_c]

print(lista_produtos)

for produto in lista_produtos:
    print("O produto é: %s e tem a cor %s e seu preco é : %.2f"%(produto[0],produto[1],produto[2]))