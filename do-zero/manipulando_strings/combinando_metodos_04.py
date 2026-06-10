# lstrip = remove espaços do início da string
# startswith = verifica se uma string inicia com alguns determinados caracteres
s1 = ' Vinicius Pozzobon Borin'
r = s1.lower().lstrip().startswith('vinicius')
print(r)