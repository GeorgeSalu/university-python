"""
Funçoes com retorno
obs:
- em python, quando uma função não retorna nenhum valor, o retorno é None
- funções python que retornam valores,devem retornar estes valores com a palavra reservada return
- não precisamos necesariamente criar uma variavel para receber o retorno de uma função. podemos passr a execução da função para outras funções

obs: sobre a palavra reservada return
- ela finaliza a função, ou seja, ela sai da execução da função
- podemos ter,numa função, diferentes returns
- podemos, numa função, retornar qualquer tipo de dado e ate mesmo multiplos valores
"""
# exemplo 1
def quadrado_de_7():
    return 7 * 7

ret = quadrado_de_7()
print(f'retorno: {ret}')

# exemplo 2
def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3
    return 'b'

print(nova_funcao())

# exemplo 3
def outra_funcao():
    return 2,3,4,5

print(outra_funcao())
print(type(outra_funcao()))

# vamor criar uma funcao pra jogar a moeda
from random import random

def jogar_moeda():
    # gera um número pseudorrandomico entre 0  e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(jogar_moeda())

# erros comuns na utilizacao do retorno, que, na verdade, nem é erro, mas sim codificação desnecessaria

def eh_impar():
    numero = 61
    if numero % 2 != 0:
        return True
    return False

print(eh_impar())