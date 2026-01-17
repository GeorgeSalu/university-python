"""
Conjuntos
- Conjuntos em qualquer linguagem de programação, estamos fazendo referência a teoria dos conjuntos da matematica
- aqui no python, os conjuntos são chamados de Sets
Dito isto, da mesma forma quena matematica
- Sets (conjuntos) não possuem valores duplicados
- Sets (conjuntos) não possuem valores ordenados
- Elementos não são acessados via indice, ou seja, conjuntos não são indexados

Conjuntos são bons para se utilizar quando precisamos armazenar elementos,
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar com
chaves, valores e itens duplicados

Os conjuntos (Sets) são referencias em Python com chaves {}

Diferença entre conjuntos (Sets) e Mapas (Dicionarios) em python:
    - Um dicionário tem chave/valor
    - Um conjunto tem apenas valor
"""
# definindo um conjunto
# forma 1
s = set({1,2,3,4,5,6,7,2,3}) # repare que temos valores repetidos
print(s)
print(type(s))

# obs: ao criar um conjunto, caso seja adicionando um valor já existente, o mesmo
# será ignorado sem gerar error e não fará parte do conjunto

# forma 2 - mais comum
s = {1,2,3,4,5,6,7,2,3}
print(s)
print(type(s))

# podemos verificar se determinado elemento esta contifo no conjuto

if 3 in s:
    print('tem o 3')
else:
    print('nao tem o 3')

# importante lembrar que, além de não termos valores duplicados, não temos ordem

# listas aceitam valores duplicados
lista = [99,2,34,23,2,12,1,44,5,34]
print(f'Lista {lista}')

# tuplas aceitam valores duplicados
tupla = 99,2,34,2,12,1,44,5,34
print(f'Tupla {tupla}')

# dicionarios nõo aceitam chaves duplicadas
dicionario = {}.fromkeys([99,2,34,2,12,1,44,5,34],'dict')
print(f'Dicionario {dicionario}')

# conjuntos não aceitam valores duplicados
conjunto = {99,2,34,2,12,1,44,5,34}
print(f'Conjunto {conjunto}')


# assim como todos outro conjunto python podemos colocar tipos de dados misturados em Sets
s = {1,'b',True,33.3,44}
print(s)
print(type(s))

# podemos interar num set normalmente
for valor in s:
    print(valor)

# usos interessantes com sets

# imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade numa lista python, já que numa lista podemos adicionar novos elementos
# e ter repetição

cidades = ['belo horizonte','sao paulo','campo grande','cuiaba','sao paulo','cuiaba']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, unicas, temos
# o que você faria ? Faria um loop na lista ... ?
# Podemos utilizar o set para isso

print(len(set(cidades)))