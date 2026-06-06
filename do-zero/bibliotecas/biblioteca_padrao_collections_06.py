# deque(maxlen) (Buffer circular)
# Cria uma fila com limite máximo de itens. Ao adicionar um novo elemento quando cheia, o item mais antigo é descartado automaticamente.
from collections import deque

buffer = deque(maxlen=3)
buffer.extend([1, 2, 3])
buffer.append(4)
print(buffer) 