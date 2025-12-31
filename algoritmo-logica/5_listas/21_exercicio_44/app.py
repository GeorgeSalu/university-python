"""
crie um programa que busca por um elemento
o metodo de loop precisa ser for
imprima a mensagem com o elemento encontrado
"""
numeros = [100,200,300,400,500,600]

qual_numero_quer_encontrar = int(input("qual numero quer encontrar? "))

encontrado = False
for n in numeros:
    if n == qual_numero_quer_encontrar:
        print("O numero %d foi encontrado" % n)
        encontrado = True

if encontrado == False:
    print("nao contramos os numero %d"%qual_numero_quer_encontrar)