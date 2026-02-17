palavra = "paralelepipedo"
for letra in palavra:
    print(letra, end=", ")

aprovados = ["rafaela","pedro","renato","maria"]
for nome in aprovados:
    print(nome, end=", ")

for posicao, nome in enumerate(aprovados):
    print(posicao+1, nome)

dias_semana = ('domingo','segunda','terca','quarta','quinta','sexta','sabado')
for dia in dias_semana:
    print(f'Hoje é {dia}')

for numero in {1,2,3,4,5,6,7}:
    print(numero)