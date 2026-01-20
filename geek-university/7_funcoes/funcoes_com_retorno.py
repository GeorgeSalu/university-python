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
def quadrado_de_7():
    return 7 * 7

ret = quadrado_de_7()
print(f'retorno: {ret}')