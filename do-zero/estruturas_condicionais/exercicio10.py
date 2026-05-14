# Exercício 10
# Uma loja de departamentos está oferecendo diferentes formas de pagamento
# conforme opções listadas a seguir
# faça um algoritmo que leia o valor total de uma compra e calcule o valor de pagamento final
# conforme a opção escolhida
# pagamento a vista - conceder desconto de 5 %
# pagamento em 3x - valor não sofre alterações
# pagamento em 5x - acréscimo de 2%
# pagamento em 10x - acréscimo de 8%

print("pagamento")
print("1 - a vista")
print("2 - parcelamento em 3x")
print("3 - parcelamento em 5x")
print("4 - parcelamento em 10x")
print("pressione outra tecla para sair...")

op = int(input("Qual forma de pagamento deseja fazer ? "))
valor = float(input("Qual o preco do pagamento ? "))

if op == 1:
    valor_final = valor * 0.95
    print(f"Produto comprado a vista. Total a pagar: R${valor_final}")
elif op == 2:
    valor_final = valor
    parcela = valor_final / 2
    print(f"Produto parcelado em 3x, total a pagar {valor_final}, valor parcela {parcela}")
elif op == 3:
    valor_final = valor * 1.02
    parcela = valor_final / 5
    print(f"Produto parcelado em 5x, total a pagar {valor_final}, valor parcela {parcela}")
elif op == 4:
    valor_final = valor * 1.08
    parcela = valor_final / 10
    print(f"Produto parcelado em 10x, total a pagar {valor_final}, valor parcela {parcela}")
else:
    print("opcao invalida")