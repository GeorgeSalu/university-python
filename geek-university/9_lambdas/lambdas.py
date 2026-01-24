"""
Utilizando Lambdas

Conhecidas por exepressões lambdas ou simplesmente lambdas, são funçõe sem nome, ou seja, são funções anonimas
"""
# função em python
def funcao(x):
    return 3 * x + 1

print(funcao(4))
print(funcao(7))

# expressao lambda
lambda x: 3 * x + 1

# utilizando a expressao lambda
calc = lambda x: 3 * x + 1
print(calc(4))
print(calc(7))

# podemos ter expressões lambda como multiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(nome=' angeline ', sobrenome='jolie'))
print(nome_completo(' felicity ', ' jones '))

# em funcões python podemos ter nenhuma ou várias entradas, em lambdas também

amar = lambda: 'como não amar python'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x,y,z: 3 / (1 / x + 1 / y + 1 / z)

print(amar())
print(uma(6))
print(duas(5,7))
print(tres(5,7,8))

# obs: se passarmos mais argumentos do que parametros esperados teremos TypeError

# exemplo 2
autores = ['issac asimov','ray bradbury','robert heinlein','arthur clarke','frank herbet','orson scott','douglas adams','h. g. wells','leigh']
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)