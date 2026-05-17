soma = 0
cont = 1
while cont <= 5:
    x = int(input(f"digite o {cont} numero : "))
    soma += x # equivalente : soma = soma + x
    cont += 1 # equivalente : cont = cont + 1
print(f"Somatorio : {soma}")