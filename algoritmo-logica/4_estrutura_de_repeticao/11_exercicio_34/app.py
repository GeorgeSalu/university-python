"""
crie um loop que detecta se um numero é primo ou não
numero primo é o numero que é divido apenas por ele mesmo e o numero 1
"""
numero = int(input("digite um numero : "))

divisoes = 0

contador = numero
while contador > 0:
    if numero % contador == 0:
        divisoes = divisoes + 1
    contador = contador - 1

if divisoes == 2:
    print("o numero é primo")
else:
    print("o numero não é primo")