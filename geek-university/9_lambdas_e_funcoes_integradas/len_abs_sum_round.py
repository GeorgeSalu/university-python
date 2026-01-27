"""
Len, Abs, Sum, Round

# Len
len() -> retorna o tamanho (ou seja, o número de itens) de um iteravel

# Abs
abs() -> retorna o valor absoluto de um número inteiro ou real, de forma basica, seria o seu valor real sem o sinal

# Sum
sum() -> recebe como parametro um iteravel, podendo receber um valor inicial, e retorna a soma total dos elementos, incluindo o valor inicial

obs: o valor incial default = 0
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

# exemplos sum()
print(sum([1,2,3,4,5]))
print(sum([1,2,3,4,5], 5))
print(sum([3.145, 5.677]))
print(sum([1,2,3,4,5], 5))
print(sum((1,2,3,4,5)))
print(sum({1, 2, 3, 4, 5}))
print(sum({'a':1,'b':2,'c':3}.values()))