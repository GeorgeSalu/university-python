"""
Entendendo o *args

- O *args é um parametro, como outro qualquer. Isso significa que você podera
chamar de qualquer coisa, desde que começe como asteristico.
Exemplo:
    *xis
Mas por convenção, utilizamos *args para defini-lo

Mas o que é o *args ?

O Parametro *args utilizado numa função, coloca os valores extra informados como entrada
em uma tupla, então desde já se lembre que tuplas são imutaveis
"""
# exemplo 1

def soma_todos_numeros(*args):
    print(args)

soma_todos_numeros()
soma_todos_numeros(1)
soma_todos_numeros(1,2)
soma_todos_numeros(1,2,3)

# exemplo 2

def verifica_info(*args):
    if 'geek' in args and 'university' in args:
        return 'bem-vindo geek'
    return 'eu não tenho certeza quem voce é'


print(verifica_info())
print(verifica_info(1, True, 'university', 'geek'))

# desempacotar

def soma_numeros(*args):
    return sum(args)

numeros = (1,2,3,4,5,6,7)

print(soma_numeros(*numeros))