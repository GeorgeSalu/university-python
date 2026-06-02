# Exercicio 8
# Crie um programa para controle de estoque de produtos de um estabelecimento que vende produtos de hortifruti
# Para o estoque, armazene todo dentro de um dicionario contendo listas.
# A chave deverá ser o nome de cada produto e dentro de cada lista teremos o preco e quantidade disponivel no estoque
# o estoque pode esta pre-cadastrado no sistema com a quantidade de itens a desejar.

# Simule uma compra. Peça ao usuario para digitar o nome do produto e a quantidade que deseja até que ele decida
# encerrar a compra, ao final apresente tudo na tela num formato organizado, mostrando o total a ser pago por
# produto e o total final do pedido. De baixa o sistema descontando o que foi comprado do total, imprima na tela o estoque restante

loja = {'cenoura':[100,0.99], 'brocolis':[50,3.99], 'batata':[200,0.49], 'cebola':[75,1.10] }

pedido = []
while True:
    item_nome = input("Qual o nome do produto : ")
    item_qtd = int(input("Dejesa comprar quantas unidades? : "))
    pedido.append([item_nome, item_qtd])

    res = input("Deseja adicionar mas um produto ao carrinho? [S/N] ")
    if res in 'Nn':
        break


total = 0
print('\nVendas')
for item in pedido:
    produto = item[0]
    qtd = item[1]
    preco = loja[produto][1]
    valor_produto = preco * qtd
    print(f"{produto} - {qtd} X {preco} = {valor_produto}")
    loja[produto][0] -= qtd
    total += valor_produto

print(f"Custo total : {total}")