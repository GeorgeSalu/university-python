produto = {'nome': 'caneta bic', 'preco': 3.00, 'importada': True, 'estoque': 785}

for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, valor)