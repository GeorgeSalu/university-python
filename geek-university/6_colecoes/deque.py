"""
Modulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance
"""
from collections import deque

# criando deques
deq = deque('geek')
print(deq)

# adicionando elementos no deque
deq.append('y')
print(deq)

deq.appendleft('k') # adiciona no comeco da lista
print(deq)

# remover elementos
print(deq.pop()) # remove e retorna o ultimo elemento
print(deq)