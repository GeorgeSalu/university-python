idade = int(input("qual é a sua idade : "))

if idade >= 18:
    print("voce pode entrar na balada")

    metodo_de_pagamento = input("como voce vai pagar a entrada ? ")

    if metodo_de_pagamento == "dinheiro":
        print("a fila do dinheiro é a numero 1")
    else:
        print("a fila de cartao é a numero 2")

else:
    print("voce nao pode entrar na balada")