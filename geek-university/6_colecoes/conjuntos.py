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

# imagine que fizemos um formulario de cadastro de visitantes numa feira ou museu e os visitantes
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

# adicionando elementos em um conjunto
s = {1,2,3,4,5,6,7,2,3}

s.add(4)
s.add(4) # duplicidade não gera erro, simplesmente é ignorado e não é adicionado
print(s)

# remover elementos em um conjunto
s = {1,2,3,4,5,6,7,2,3}
print(s)

# fomra 1
s.remove(3) # não é indice! informamos o valor a ser removido
print(s)

# obs: caso o valor não seja encontrado será gerado o erro KeyError

# forma 2
s.discard(2)
print(s)

# obs: se o valor não for encontrado, nenhum erro é gerado

# copiando um conjunto para outro...
s = {1,2,3,4,5,6,7,2,3}

# forma 1 - deep copy
novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# forma 2
novo = s

novo.add(4)

print(novo)
print(s)

# podemos remover todos os itens de um conjunto
s.clear()
print(s)

# metodos matematicos de conjuntos

# imagine que temos dois conjuntos: um contendo estudantes do curso python e um
# contendo estudantes do curso de java

estudantes_python = {'marcos','patricia','ellen','pedro','julia','guilherme'}
estudantes_java = {'fernendo','gustavo','julia','ana','patricia'}

# veja que alguns alunos esque estudam python também estudam java
# precisamos gerar um conjunto com nomes de estudantes unicos
# forma 1 - utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# forma 2 - utilizando o caracter pipe
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# gerar um conjunto de estudantes que estão em ambos os cursos
# forma 1 - utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# forma 2 - utilizando &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# gerar um conjunto de estudantes que não estão no outro curso
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# soma, valor maximo, valor minimo e tamanho
s = {1,2,3,4,5,6,7,2,3}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))