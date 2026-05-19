# Exercício 7
# Escreva um algoritmo que calcule a media dos números pares de 1 ate 100 (1 e 100 inclusos)
# implemente o laço usando for

soma = 0
qtd = 0

for i in range(1,101,1):
    if i % 2 == 0:
        soma = soma + i
        qtd = qtd + 1

media = soma / qtd
print(f"A media dos pares de 1 ate 100 é : {media}")