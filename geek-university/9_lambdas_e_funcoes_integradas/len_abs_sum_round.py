"""
Len, Abs, Sum, Round

# Len
len() -> retorna o tamanho (ou seja, o número de itens) de um iteravel
"""
# exemplo len()
print(len('geek university'))
print(len([1,2,3,4,5]))
print(len((1,2,3,4,5)))
print(len({1,2,3,4,5}))
print(len({'a':1,'b':2,'c':3,'d':4,'e':5}))
print(len(range(0,10)))

# por debaixo dos panos,quando utilizamos a função len() o python faz o seguinte:
# dunder len
print('geek university'.__len__())