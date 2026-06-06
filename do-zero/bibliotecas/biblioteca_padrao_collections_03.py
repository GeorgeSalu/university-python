# defaultdict (Dicionário com valores padrão)
# Evita erros de KeyError ao tentar acessar chaves que ainda não existem, definindo um tipo padrão para elas
from collections import defaultdict

dicionario = defaultdict(int)
dicionario['maça'] += 3
print(dicionario['banana'])