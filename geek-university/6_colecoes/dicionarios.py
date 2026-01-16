"""
dicionarios

obs: em algumas linguagens de programacao, os dicionarios pyhton são conhecidos como mapas

dicionarios são coleções do tipo chave/valor
dicionarios são representados por chaves {}
print(type({}))

obs: sobre dicionarios
 - chave e valor são separados por dois pontos 'chave:valor'
 - tanto chave quanto valor podem ser de qualquer tipo de dado
 - podemos misturar tipos de dados
"""
#  criacao de dicionarios
# forma 1 (mais comum)
paises = {'br': 'brasil', 'eua': 'estados unidos', 'py':'paraguai'}
print(paises)
print(type(paises))

# forma 2 (menos comum)
paises = dict(br='brasil', eua='estados unidos', py='paraguai')
print(paises)
print(type(paises))

# acessando elementos
# forma 1 - acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['eua'])

# obs: caso tentarmos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# forma 2 - acessando via get - recomendado
print(paises.get('br'))
print(paises.get('eua'))