"""
crie um programa que recebe a categoria, em valor numerico, de produto
se for 1: exiba que uma bolsa
se for 2: exiba que um tenis
se for 3: exiba que é uma mochila
caso nao seja nenhum dos valores, exiba que a categoria noa foi encontrada
"""
categoria = int(input("Qual o número da categoria? "))

print(categoria)

if categoria == 1:
  print("Este produto é da categoria BOLSA")
elif categoria == 2:
  print("Este produto é da categoria TÊNIS")
elif categoria == 3:
  print("Este produto é da categoria MOCHILA")
else:
  print("Categoria não encontrada!")