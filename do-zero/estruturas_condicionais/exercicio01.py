# Exercício 1
# desenvolva um algoritmo que seja capaz de calcular a soma e a subtracao entre 2 valores com vírgula
# crie duas variáveis de teste, uma que teste se a soma é maior do que 10
# outra que testa se a subtração é maior do que 0. Imprima tudo na tela

x = float(input("Digite o primeiro numero : "))
y = float(input("Digite o segundo numero : "))

soma = x + y
subtracao = x - y
print(f"Soma : {soma:.2f} Subtracao: {subtracao:.2f}")

if soma > 10:
    print(f"A soma é maior do que 10")

if subtracao < 0:
    print(f"A subtracao é menor do que 0")