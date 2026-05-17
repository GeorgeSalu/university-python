# validando a entrada
x = int(input("digite um valor maior do que zero : "))
while x <= 0:
    x = int(input("digite um valor maior que zero : "))
print(f"voce digitou {x}. encerrando o programa")