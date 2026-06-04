# são tratados como False/Falsey
# - O número zero, seja ele inteiro ou ponto flutuante
# - Uma string sem nenhum conteúdo
# - tuplas vazias
# - listas vazias
# - dicionarios vazios
# - intevalos vazios

# Todos estes retornam False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool([]))
