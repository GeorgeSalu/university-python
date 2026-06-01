game = {}
games = []

for i in range(2):
    game['nome'] = input('qual o nome do jogo: ')
    game['videogame'] = input('para qual o videogame ele foi lancado : ')
    game['ano'] = input('qual o ano do jogo: ')
    games.append(game)
print('-'*20)

for jogos in games:
    for chave, valor in jogos.items():
        print(f'{chave} - {valor}')