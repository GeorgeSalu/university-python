"""
**Kwargs

Poderiamos chamar este parametro de **xis, m por convenção chamamos de **kwargs

Este é so, mas um parametro, mas diferente do *args que coloca os valores extras
em tuplas, o **kwargs exige que utilizemos parametros nomeados, e transforma esses
paramatros extras em um dicionário
"""
# exemplos

def cores_favoritas(**kwargs):
    print(kwargs)

cores_favoritas(marcos='verde',julia='amarelo',fernando='azul',vanessa='branco')

# obs: os parametros *args e **kwargs não são obrigatorios

# exemplo mas complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'python':
        return 'voce recebeu um cumprimento pythonico geek'
    elif 'geek' in kwargs:
        return f'{kwargs['geek']} geek'
    return 'não tenho certeza quem voce é ....'


print(cumprimento_especial())
print(cumprimento_especial(geek='python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))

"""
Nas nossas funções, podemos ter (nesta ordem)

- parametros obrigatorios
- *args
_ Parametros default (não obrigatorios))
- **kwargs
"""

def minha_funcao(idade, nome, *args, solteiro=False,**kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)

minha_funcao(8, 'julia')
minha_funcao(18,'felicity', 4,5,2, solteiro=True)
minha_funcao(34, 'Felipe',eu='nao', voce='vai')
minha_funcao(19,'carla',9,4,3,java=False,python=True)

# desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} tem {kwargs['sobrenome']} "

nomes = {'nome': 'george', 'sobrenome': 'silva'}
print(mostra_nomes(**nomes))