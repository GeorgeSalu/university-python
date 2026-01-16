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

# concatenacao de tuplas
tupla1 = (1,2,3,4,5,6)
print(tupla1)

tupla2 = (7,8,9,0)
print(tupla2)

print(tupla1 + tupla2) # tuplas são imutaveis
print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2 # tuplas são imutaveis, mas podemos sobrescrever os seus valores
print(tupla1)

# verificar se determinado elemento esta contido na tupla
tupla = (1,2,3,4,5,6)
print( 3 in tupla)

# iterando sobre uma tupla
tupla = (1,2,3,4,5,6)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# contando elementos dentro de uma tupla
tupla = ('a','b','c','d')

print(tupla.count('a'))

escola = tuple('geek university')
print(escola)

print(escola.count('e'))

# dicas na utilizacao de tuplas
# devemos utilizar sempre que não precisamos modificar os dados contidos em uam coleção
# exemplo 1
meses = ('janeiro', 'fevereiro','marco','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
