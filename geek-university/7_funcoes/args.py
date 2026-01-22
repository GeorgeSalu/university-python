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
# exemplos

def soma_todos_numeros(*args):
    print(args)

soma_todos_numeros()
soma_todos_numeros(1)
soma_todos_numeros(1,2)
soma_todos_numeros(1,2,3)
