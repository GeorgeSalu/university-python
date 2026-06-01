# Exercicio 4
# Escreva um algoritmo que crie uma lista vazia e ca adicionando valores referentes
# a ota de um aluno nesta lista. Quando o usuario desejar parar de digitar nota
# (digitando um valor negativo, por exemplo), calcule a média das notas digitadas

notas = list()
x = float(input("Digite uma nota: "))
while x >= 0:
    notas.append(x)
    x = float(input("Digite uma nota: "))

soma = 0
for valores in notas:
    soma += valores

media = soma / len(notas)
print(notas)
print(f"Media das notas digitadas: {media}")