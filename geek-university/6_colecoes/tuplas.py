"""
tuplas (tuple)

tuplas são bastant parecidas com listas
existem basicamentes duas diferenças basicas
1 - as tuplas são representadas por parenteses ()
2 - as tuplas são imutaveis: isso significa que ao se criar uma tupla ela não muda. toda a operação em uma tupla gera uma nova tupla
"""
# cuidado 1: as tuplas são representadas por (). mas veja
tupla1 = (1,2,3,4,5,6)
print(tupla1)
print(type(tupla1))

tupla2 = 1,2,3,4,5,6
print(tupla2)
print(type(tupla2))

# cuidado 2: tuplas com 1 elemento
tupla3 = (4)
print(tupla3)
print(type(tupla3))

tupla4 = (4,)
print(tupla4)
print(type(tupla4))
# conclusão: podemos concluir que tuplas são definidas pela vigula e não pelo usuo do parenteses

# podemos gerar uma tupla dinamicamente com range(inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# desempacotamento de tupla
tupla = ('geek university',"programacao python")

escola, curso = tupla
print(escola)
print(curso)

# obs: gera erro(ValueError) se colocarmos um numero diferente de elementos para desempacotar

# metodos para adição e remoção de elemetos nas tuplas não existem, dado o fato que as tuplas são imutaveis

# soma, valor maximo, valor minimo e tamanho
tupla = (1,2,3,4,5,6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))