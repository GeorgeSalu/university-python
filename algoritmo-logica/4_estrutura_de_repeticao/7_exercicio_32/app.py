"""
escreva um loop while que vai de 20 a 0
quando encontrar o numero 5 cancele o loop
imprima os numeros na tela
"""
n = 20

while n >= 0:
  print(n)

  if n == 5:
    break

  n = n - 1

print("Pós loop")