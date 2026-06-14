# find() = procurar se uma substring esta dentro de outra string, e retorna a posicção da primeira ocorrencia
# Você pode limitar a área da busca passando um ponto de início e um ponto final.
frase = "Python é uma linguagem incrível."
# Busca a letra "a" apenas entre os índices 5 e 20
posicao = frase.find("a", 5, 20)

print(posicao)