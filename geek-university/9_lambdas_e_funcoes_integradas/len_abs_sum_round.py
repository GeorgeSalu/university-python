"""
Len, Abs, Sum, Round

# Len
len() -> retorna o tamanho (ou seja, o número de itens) de um iteravel

# Abs
abs() -> retorna o valor absoluto de um número inteiro ou real, de forma basica, seria o seu valor real sem o sinal
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

# exemplo abs()
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))