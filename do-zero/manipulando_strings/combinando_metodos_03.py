# strip() = remove espaços do início e fim da string
# startswith() = verifica se uma string inicia com alguns determinados caracteres
s1 = ' Vinicius Pozzobon Borin '
r = s1.lower().strip().startswith('vinicius')
print(r)