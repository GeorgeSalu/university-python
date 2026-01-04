def soma(a,b):
    return a+b

def multiplicacao(a,b):
    return a*b

def operacao(a,b,f):
    resultado = f(a,b)
    return resultado

a = operacao(1,2,soma)
print(a)

b = operacao(10,5,multiplicacao)
print(b)