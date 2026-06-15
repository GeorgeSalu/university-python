# isdecimal() = verifica se todos os caracteres de uma string são numéricos decimais (de 0 a 9).

texto = "12345"
resultado = texto.isdecimal()
print(resultado)

texto = "100A"
resultado = texto.isdecimal()
print(resultado)

texto = "12.34"
resultado = texto.isdecimal()
print(resultado)