def calcular(a,b):
    soma = a + b
    multiplicacao = a * b
    return soma, multiplicacao


# programa principal
resultado_soma, resultado_multiplicacao = calcular(4,5)
print(f"resultado_soma: {resultado_soma}, resultado_multiplicacao: {resultado_multiplicacao}")