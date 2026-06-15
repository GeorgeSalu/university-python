# isspace() = verifica se uma string contém apenas espaços em branco (como espaços simples  , tabulações \t ou quebras de linha \n).
# Ele retorna True se todos os caracteres forem espaços e houver pelo menos um caractere, ou False caso contrário.

texto = "   "
print(texto.isspace())

texto_formatado = "\t \n"
print(texto_formatado.isspace())

texto_mesclado = "Olá "
print(texto_mesclado.isspace())