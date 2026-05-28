item = []
mercado = list()

for i in range(3):
    item.append(input('digite o nome do item : '))
    item.append(int(input('digite a quantidade : ')))
    item.append(float(input('digite o valor : ')))
    mercado.append(item[:])
    item.clear()
print(mercado)