# Counter (Contagem de elementos)
# Ideal para contar a frequência de itens em listas ou strings
from collections import Counter

lista = ['maçã', 'banana', 'maçã', 'laranja', 'banana', 'maçã']
contagem = Counter(lista)
print(contagem)