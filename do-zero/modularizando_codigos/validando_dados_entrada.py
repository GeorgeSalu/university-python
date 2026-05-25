def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x


# programa principal
x = valida_int('digite um valor inteiro : ', 0, 100)
print(f"voce digitou o valor {x}, encerrando o programa....")