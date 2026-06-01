game = {'nome':'super mario','desenvolvedora':'nintendo','ano':1990}

print(game.values())

for i in game.values():
    print(i)

print('----------------------------------')

for i,j in game.items():
    print(f"{i} - {j}")