"""
escreva um programa que recebe um numero
verifique se o numero é maior que 10,se nao for imprim uma mensagem avisando que para prosseguir precisa se maior que 10
no primeiro if verifique se o numero é menor que 20, e imprima a multiplicacao dele por 2
se nao imprima o numero multiplicador por 5
"""
numero = int(input("insira um numero: "))

print(numero)

if numero > 10:

    if numero > 20:
        print("numero maior que 20")
        print(numero * 2)
    else:
        print("numero menor que 20")
        print(numero * 5)

else:
    print("o numero precisa ser maior que 10")