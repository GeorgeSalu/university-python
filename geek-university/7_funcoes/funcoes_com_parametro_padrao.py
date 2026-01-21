"""
Funcoes com parametro padrao (Default Parameters)

_ Funções onde a passagem de parametro seja opcional

# exemplo de função onde a passagem de parametro seja opcional
print('geek university')
print()

# exemplo de função onde a passagem de parametro seja obrigatori
def quadrado(numero):
    return numero * numero

print(quadrado(3))
print(quadrado()) # TypeError
"""
# obs: em python os parametros com valores default devem sempre estar ao final da declaração

def teste(potencia, num=2):
    return num ** potencia

print(teste(6))

# exemplos mas complexos
def mostrar_informacao(nome='geek',instrutor=False):
    if nome == 'geek' and instrutor:
        return 'bem vindo instrutor geek'
    elif nome == 'geek':
        return 'eu pensei que voce era o instrutor'
    return f'ola {nome}'

print(mostrar_informacao())
print(mostrar_informacao(instrutor=True))
print(mostrar_informacao(True))
print(mostrar_informacao('Ozzy'))
print(mostrar_informacao(nome='stephany'))