# Exercício 12
# Escreva um algoritmo que obtenha do usuario uma frase de tamanho entre 10 e 30 caractres
# (faça a validação deste dado)
#
# após a frase ter sido digitada corretamente,
# faça a impressão dela na tela de maneira exata como foi digitada e, em seguida,
# remova os espaços da frase e imprima novamente, sem espaços

frase = input("digite uma frase: ")
tamanho = len(frase)
while (tamanho < 10) or (tamanho < 30):
    frase = input("digite uma frase: ")
    tamanho = len(frase)

print(f"com espacos: {frase}")
print(f"sem espacos: {frase}", end='')
for i in range(0, tamanho):
    if frase[i] != ' ':
        print(frase[i], end="")