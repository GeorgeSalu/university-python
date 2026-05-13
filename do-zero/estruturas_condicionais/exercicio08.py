# Exercício 8
# Escreva um algoritmo que o usuário escolhe se ele quer comprar maças, larnjas ou bananas.
# Devera ser apresentado na tela um menu com a opção 1 para maça, 2 para laranja e 3 para banana
# Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar
# O algoritmo deve calcular o preço total a pagar do produto escolhido e mostrá-lo na tela
# Considere que uma maça custa 2,30, uma laranja 3,60 e uma bananas 1,85

print("escolha a fruta que deseja comprar:")
print("1 - Maça")
print("2 - Laranja")
print("3 - Banana")

produto = int(input("Qual sua escolha ?"))
qtd = int(input("Quantas unidades deseja comprar ? "))

if produto == 1:
    pagar = qtd * 2.3
    print(f"Voce comprou {qtd} maças. total a pagar {pagar}")
elif produto == 2:
    pagar = qtd * 3.6
    print(f"Voce comprou {qtd} laranja. total a pagar {pagar}")
elif produto == 3:
    pagar = qtd * 1.86
    print(f"Voce comprou {qtd} banana. total a pagar {pagar}")
else:
    print("Produto inexistente")