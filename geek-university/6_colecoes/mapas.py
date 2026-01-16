"""
mapas -> conhecidos em python como dicionarios

dicionarios em python são representados por chaves {}
"""
receita = {'jan': 100, 'fev': 200, 'mar': 300}

# interar sobre dicionarios
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'em {chave} recebi R$ {receita[chave]}')