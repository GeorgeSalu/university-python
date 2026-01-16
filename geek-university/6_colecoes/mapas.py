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

# acessando as chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)


# desempacotamento de dicionarios
for chave, valor in receita.items():
    print(f'chave= {chave} valor= {valor}')

# soma, valor maximo, valor minimo, tamanho
# se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))