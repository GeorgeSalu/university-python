mercado = []

for i in range(3):
    nome = input('Digite o nome do item : ')
    qtd = int(input('Digite a quantidade : '))
    valor = float(input('Digite o valor : '))
    mercado.append([nome, qtd, valor])

# qual o nome do primeiro produto
print(mercado[0][0])

# quanto custa um tomate
print(mercado[1][2])

# quanso sacos de arroz foram comprados 
print(mercado[2][1])