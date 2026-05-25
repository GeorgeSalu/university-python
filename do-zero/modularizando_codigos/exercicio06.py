# Exercício 6
# Faça uma função que recebe dois valores inteiros e positivos como parametro.
# Calcule a soma dos n valores inteiros existentes entre eles, inclusive estes números

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    return x

def soma(inicio, fim):
    soma = 0
    i = inicio
    while i <= fim:
        soma += i
        i += 1
    return soma

# programa principal
x = valida_int('digite um valor inteiro e positivo : ', 1,9999)
y = valida_int('digite um segundo valor inteiro e positivo : ', 1,9999)
print(f"Somatoria entre os valores {x} e {y} é {soma(x, y)}")