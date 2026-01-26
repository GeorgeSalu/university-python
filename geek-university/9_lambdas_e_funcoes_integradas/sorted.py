"""
Sorted

obs: não confunda, apesar do nome,com a função sort() que já estudamos em listas, o sort()
so funciona em listas.

Podemos utilizar o sorted() com qualquer iteravel

Como o proprio nome diz, sorted() serve para ordenar.

obs: o sorted() sempre retorna uma lista com os elementos do iteravel ordenados
"""
# exemplo
numeros = [1,2,102,9,4,6]
print(numeros)
print(sorted(numeros)) # ordena do menor para o maior
print(numeros)

# adionando parametros ao sorted()
numeros = [6,1,8,2]
print(numeros)
print(sorted(numeros, reverse=True)) # ordena do maior para o maior

# podemos utilizar o sorted() para coisas mais complexas
usuarios = [
    {"username": "samuel", "tweets": ["eu adoro bolos", "eu adoro pizzas"]},
    {"username": "carla", "tweets": ["eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bobo123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["eu gosto de cachorros", "vou sair hoje"]},
    {"username": "gal", "tweets": [],"cor": "preto", "musica": "samba"},
]
print(usuarios)

# ordenando por usuario
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# exemplo 2
musicas = [
    {"titulo": "thunderstructk", "tocou": 3},
    {"titulo": "Dead skin mask", "tocou": 2},
    {"titulo": "Back in black", "tocou": 4},
    {"titulo": "too old to rock", "tocou": 32},
]

# ordenar da menos tocada para a mais tocada
print(sorted(musicas, key=lambda music: music["tocou"]))

# ordenar da mais tocada para a menos tocada
print(sorted(musicas, key=lambda music: music["tocou"], reverse=True))