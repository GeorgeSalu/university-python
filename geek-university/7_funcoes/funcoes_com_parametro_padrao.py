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

# por que utilizar parametros com valor default ?
# - nos permite ser, mas flexivel nas funções
# - evita erros com parametros incorretos
# - nos permite trabalhar com exemplos, mas legiveis de codigo

# quais tipos de daos podemos utilizar como valores default para parametros ?
# - qualquer numero de dados : numero, string, float, boolean, etc...

# exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(3,4))
print(mat(3,4, subtracao))

# podemos ter funcoes que são declaradas dentro ed funcções, e também tem uma forma especial de escopo de varaivel

def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador += 1
        return contador
    return dentro()

print(fora())