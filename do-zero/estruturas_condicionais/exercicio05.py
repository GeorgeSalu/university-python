# Exercício 5
# Escreva um algoritmo que le um valor inteiro qualquer
# Após verifique se este valor está contido dentro dos seguintes intervalos: -100 < x < -1 ou 1 < x < 100
# imprima na tela uma mensagem caso ele esteja em um dos intervalos

x = int(input("digite um valor inteiro : "))
if ((x > 1) and (x < 100)) or ((x < -1) and (x > -100)):
    print("um dos criterios de intervalo foi atingido")