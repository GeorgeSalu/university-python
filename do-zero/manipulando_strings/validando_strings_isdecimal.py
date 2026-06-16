# isdecimal() = verifica se todos os caracteres de uma string são numéricos decimais (de 0 a 9). Ele retorna True apenas se a string
# contiver exclusivamente números e não possuir letras, espaços ou símbolos, sendo útil para validar entradas de dados numéricos

texto = "12345"
resultado = texto.isdecimal()
print(resultado)

texto = "100A"
resultado = texto.isdecimal()
print(resultado)

texto = "12.34"
resultado = texto.isdecimal()
print(resultado)