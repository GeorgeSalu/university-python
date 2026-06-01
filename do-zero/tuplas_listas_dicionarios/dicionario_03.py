game = {'nome':'super mario','desenvolvedora':'nintendo','ano':1990}

print('--------------chaves do dicionario------------------------------')
for chave in game.keys():
    print(chave)

print('--------------valores do dicionario-----------------------------')
for valor in game.values():
    print(valor)

print('--------------chaves e valores do dicionario--------------------')
for chave,dado in game.items():
    print(f"{chave} - {dado}")