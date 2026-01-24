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
media = statistics.median(dados)
print(media)