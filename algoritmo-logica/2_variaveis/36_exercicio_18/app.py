"""
Crie um programa que recebe o saldo de uma conta bancaria com R$ 359.56
deposi insira uma nova quantia por meio de input
e remova uma valor de R$ 125.98, referente a fatura de cartao de credito
imprima o valor na tela
"""
saldo = 359.56

deposito = float(input('Informe o valor do deposito: '))

print(saldo)
print(deposito)

saldo = saldo + deposito
print(saldo)

fatura_cartao = 125.98
saldo = saldo - fatura_cartao
print("o saldo restante é %.2f" %saldo)