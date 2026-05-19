# Exercício 10
# Escreva um algoritmo que repetidamente pergunte ao usuário qual a sua idade e o seu sexo (M ou F)
# para cada resposta o programa deve imprimir a mensagem
# "Boa noite, senhor, a sua idade é <IDADE>" caso género masculino
# "Boa noite, senhora, a sua idade é <IDADE>" caso género feminino
#
# O programa deve encerrar quando o usuário digitar uma idade negativa

idade = int(input("digite sua idade: "))
while idade > 0:
    sexo = input("digite seu sexo (M/F): ")
    if sexo == "M":
        print("seu sexo: Masculino")
    else:
        if  sexo == "F":
            print("seu sexo: Feminino")
        else:
            print("opcao invalida")
    idade = int(input("digite sua idade: "))

print("encerrado")