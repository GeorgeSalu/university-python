# namedtuple (Tuplas nomeadas)
# Cria tuplas cujos elementos podem ser acessados por nomes (como atributos), deixando o código mais claro do que usar índices numérico
from collections import namedtuple

Ponto = namedtuple('Ponto', ['x', 'y'])
p = Ponto(10, 20)
print(p.x, p.y)  # Saída: 10 20