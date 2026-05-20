# Exercício 13
# escreva um algoritmo que leia inteiros via teclado
# somente valores positivos devem ser aceites pelo programa
# o final da execução, informe a média dos valores digitados

soma = 0
qtd = 0

while True:
    x = int(input("digite um valor inteiro e positivo: "))
    if not x:
        break

    soma += x
    qtd += 1

media = soma / qtd
print(f"a media dos valores digitados é {media}")