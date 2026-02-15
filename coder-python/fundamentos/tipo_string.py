print(dir(str))
nome = 'saulo pedro'
print(nome)
print(nome[0])

texto = """
Texto em multiplas 
linhas
"""
print(texto)

doc = '''
tambem é possivel 
com 3 spas simples
'''
print(doc)

nome = "Ana paula"
print(nome[0])
print(nome[6])
print(nome[-3])
print(nome[4:])
print(nome[-5:])
print(nome[:3])
print(nome[2:5])

numeros = '1234567890'
print(numeros)
print(numeros[::])
print(numeros[::2])
print(numeros[1::2])
print(numeros[::-1])
print(numeros[::-2])


frase = 'Python é uma linguagem excelente'
print('py' not in frase)
print('ing' in frase)
print(len(frase))
print(frase.lower())
print(frase.upper())

# metodos magicos
a = '123'
b = ' de oliveira 4'
print(a + b)
print(a.__add__(b))
print(str.__add__(a, b))
print(len(a))
print(a.__len__())
print('1' in a)
print(a.__contains__('1'))