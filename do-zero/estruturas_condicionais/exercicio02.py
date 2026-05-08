# Exercício 2
# desenvolva um algoritmo que solicite o seu ano de nascimento e o ano atual. Calcule a sua idade e apresente na tela
# para fins de simplificação, despreze o dia e o mes do ano
# após o cálculo, verifique se a idade é maior ou igual a 18 ano e apresente na tela uma mensagem
# imformando que já é possivel tirar a carteira de motorista caso seja maior

ano_nascimento = int(input("Qual o seu ano de nascimento ? "))
ano_atual = int(input("Em qual ano estamos ? "))
idade = ano_atual - ano_nascimento

print(f"Voce tem {idade} anos de idade.")
if idade >= 18:
    print("vc pode ter carteira de motorista")