"""
Modulo Collections = Default Dict

# recap dicionario
dicionario = {'curso':'curso de python'}
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro']) # KeyError

Default Dict -> Ao criar um dicionario utilizando-o, nós informamos um valor default, podendo
utilizar um lambda para isso, esse valor sera utilizado sempre que não houver um valor definido.
Caso tentemos acessar uma chave que não existe, essa chave será criada e o valor default será atribuído

obs: lambda são funções sem nome, que podem ou não receber parametros de entrada e retornar valores
"""
# fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda : 0)
print(dicionario)

dicionario['curso'] = 'curso de python'
print(dicionario)

print(dicionario['outro']) # não retorna erro
print(dicionario)