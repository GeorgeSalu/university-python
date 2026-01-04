"""
escreva uma funcao que desenha uma escada no terminal
os numeros de degraus deve informados por parametros
"""
def criar_escada(degraus):
    i = 1
    while i <= degraus:
        print("#"*i)
        i += 1

criar_escada(3)
print("------------------------------")
criar_escada(10)