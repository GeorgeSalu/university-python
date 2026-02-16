tupla = tuple()
tupla = ()
print(type(tupla))
print(dir(tupla))

tupla = ('um')
print(type(tupla))
tupla = ('um',)
print(type(tupla))

cores = ('verde', 'amarelo', 'azul')
print(cores[0])
print(cores[-1])
print(cores[1:])

print(cores.count('verde'))
print(len(cores))