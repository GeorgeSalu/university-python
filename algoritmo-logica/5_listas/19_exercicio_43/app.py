"""
crie uma lista com alguns items
peça dois itens ao usuario
identifique qual foi encontrado primeiro na lista
"""
itens_carro = ["porta","pneu","estepe","macaneta","janela","chave","motor","marcha"]

item_um = input("o que deseja procurar primeiro ? ")
item_dois = input("o que deseja procurar depois ? ")

i = 0

while i < len(itens_carro):
    if itens_carro[i] == item_um:
        print("O primeiro objetoi foi encontrado antes!%s"%item_um)
        break
    else:
        print("O segundo objeto foi encontrado antes!%s"%item_dois)
        break

    i = i + 1