"""
Filter

filter() -> serve para filtrar dados de uma determinada coleção
"""
# biblioteca para trabalhar com dados estatiticos
import statistics
# exemplo 1
valores = 1, 2, 3, 4, 5, 6
media = (sum(valores))/len(valores)
print(media)

# exemplo 2
dados = [1.3,2.7,0.8,4.1,4.3,-0.1]

# calculando a média dos dodos utilizando a função mean()
media = statistics.mean(dados)
print(f'media = {media}')

# obs: assim como a função map() a filter() recebe dois parametros, sendo
# uma função e um iteravel

res = filter(lambda x: x > media, dados)
print(type(res))
print(list(res))

# obs: assim como na função map(), apos serem utilizados dos dados de filter() eles são excluidos da memória

#exemplo 3
paises = ['','argentina','','brasil','chile','','colombia','','equador','','','venezuela']
print(paises)

# forma 1 - filtra os vazios
res = filter(None, paises)
print(list(res))

# forma 2 - filtro os vazios
res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

# forma 3 - filtra os vazios
res = filter(lambda pais: pais != '', paises)
print(list(res))

# a diferenca entre map() e filter() é:
# map() -> recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável
# filter() -> recebe dois parâmetros, uma função e iterável e retorna um objeto filtrando apenas os elementos de acordo com a função

# exemplos mais complexos
usuarios = [
    {"username": "samuel", "tweets": ["eu adoro bolos", "eu adoro pizzas"]},
    {"username": "carla", "tweets": ["eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bobo123", "tweets": []},
    {"username": "doggo", "tweets": ["eu gosto de cachorros", "vou sair hoje"]},
    {"username": "gal", "tweets": []},
]

print(usuarios)
# filtrar os usuarios que estão inativos no twitter

# forma 1
inativos = list(filter(lambda usuario: len(usuario["tweets"]) == 0, usuarios))
print(inativos)

# forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

# combinando filter() e map()

nomes = ['vanesa','ana','maria']

# devemos criar uma lista contendo 'a sua instrutora é'+nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)