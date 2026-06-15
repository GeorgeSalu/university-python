# isupper() = retorna True apenas se todos os caracteres da string puderem ser exibidos na tela de forma visível e não forem
# caracteres de controle ocultos (como quebras de linha ou tabulações). Se a string estiver vazia, ela também retorna True

texto = "Olá, mundo!"
print(texto.isprintable())

texto_com_enter = "Linha 1\nLinha 2"
print(texto_com_enter.isprintable())

texto_vazio = ""
print(texto_vazio.isprintable())