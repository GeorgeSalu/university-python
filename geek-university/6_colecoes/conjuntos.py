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