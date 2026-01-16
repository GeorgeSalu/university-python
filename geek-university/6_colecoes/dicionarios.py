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

russia = paises.get('ru')

# podemos definir um valor padrao para caso nao encontremos o objeto com a chave informada
# caso o get não encontre o objeto com a chave informada sera retornado o valor None e não sera gerado KeyError
russia2 = paises.get('ru','não encontrado')

if russia:
    print('encontrei o pais')
else:
    print('nao encontrei o pais')


# podemos verificar se determinada chave se encontra em um dicionario
print('br' in paises)
print('ru' in paises)
print('estados unidos' in paises)

# podemos utilizar qualquer tipo de dado (int, float, string, boolean) inclusive lista, tupla, dicionario

localidades = {
    (35.6895, 39.6917): 'escritorio em tokio',
    (40.7128, 74.0060): 'escritorio em nova york',
    (37.7749, 122.4194): 'escritorio em sao paulo',
}

print(localidades)
print(type(localidades))

# tuplas, por exemplo, são btante interessantes de serem utilizadas como chave de dicionários, pois as mesmas são imutaveis

# adicionando elementos em um dicionário

receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(receita)
print(type(receita))

# forma 1
receita['abr'] = 350
print(receita)

# forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)