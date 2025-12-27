"""
crie um programa que recebe  renda do usuario
baseado na renda ele vai liberar um limite para o cartao de credito
se for menos que 2000, 1000 de limite
menos de 4000, 2000 de limite
menos de 6000, 3000 de limite
se for menos que 10000, insira uma mensagem para falar com gerente
"""
renda = float(input("Digite a sua renda: "))

print(renda)

limite = 0

if renda < 2000:
  limite = 1000
elif renda < 4000:
  limite = 2000
elif renda < 10000:
  limite = 3000
elif renda > 10000:
  print("Você precisa falar com o nosso gerente")
  limite = 3000

print("O seu cartão foi aprovado, e o limite é de R$%d" % limite)