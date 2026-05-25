# Exercício 5
# Factorial é um número inteiro positivo, representado por n!
# Calculamos a factorial pela multiplicação desse numero n por todas os seus antecessores ate chegar em 1.
# Ainda, factorial de 0! Sempre será 1
# Considerando a breve explicação sobre factorial,
# Escreva uma função que calcule a factorial de um número recebido como paramentro e retorne o seu resultado
# faça uma validação dos dados atraves de uma outra função, permitindo que somente valores positivos sejam aceites

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    return x


def factorial(num):
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num + 1, 1):
        fat *= i
    return fat



# programa principal
x = valida_int('digite um valor para calcular a fatorial : ', 0, 999)
print(f"{x}! = {factorial(x)}")
