"""
crie um programa com recebe dois numeros
insira a multiplicacao entre eles em uma varivel
se for menor ou igual a 100 o resultado insira uma mensagem de que o numero é baixo
se nao o numero é alto
"""
numero_um = int(input('Digite o primeiro numero: '))
numero_dois = int(input('Digite o segundo numero: '))

multiplicacao = numero_um * numero_dois
print(multiplicacao)

if multiplicacao <= 100:
    print("o numero é baixo, o numero é %d"%multiplicacao)
else:
    print("o numero e alto, o numero é %d"%multiplicacao)