# exercício 3
# desenvolva um algoritmo que solicite ao usuario o preco de um produto
# e um percentual de desconto a ser aplicado a ele
# calcule e exiba o valor do desconto e o preço final do produto

preco = float(input("digite o preco do produto : "))
p = float(input("digite o percentual de desconto (0 - 100%): "))

desconto = preco * (p/100)
final = preco - desconto

print(f"O preco do produto é {preco}, desconto aplicado de {p}%")
print(f"Valor de desconto calculado: {desconto}")
print(f"valor final do produto: {final}")