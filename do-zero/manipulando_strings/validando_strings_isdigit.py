# isdigit() = verifica se todos os caracteres de uma string são numéricos. Ele retorna True se a string não estiver vazia e contiver
# apenas dígitos, ou False caso contrário. É muito usado para validar entradas antes de converter strings para números
entrada = "25"
print(entrada.isdigit())

entrada2 = "9988-abcd"
print(entrada2.isdigit())

entrada3 = "12³"
print(entrada3.isdigit())