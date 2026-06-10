# rstrip() = remove espaços do fim da string
# endswith() = verifica se uma string termina com alguns determinados caracteres
s1 = 'Vinicius Pozzobon Borin '
r = s1.lower().rstrip().endswith('borin')
print(r)