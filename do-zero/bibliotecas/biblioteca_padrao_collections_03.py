# deque (Fila dupla)
# Uma lista otimizada para inserções e remoções rápidas em ambas as extremidades (início e fim).
from collections import deque

fila = deque(['Ana', 'Bruno', 'Carlos'])
fila.append('Diana')  # Adiciona no final
fila.popleft()        # Remove no início (muito rápido)
print(fila)           # Saída: deque(['Bruno', 'Carlos', 'Diana'])