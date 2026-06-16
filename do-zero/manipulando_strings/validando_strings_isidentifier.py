# isidentifier() = verifica se uma string é um identificador válido.Retorna True se a string contiver apenas letras, números
# e underscores, e não começar com um número. Ele é muito usado para validar nomes de variáveis, funções ou chaves em parsers

nome_valido = "minha_variavel_1"
print(nome_valido.isidentifier())

nome_invalido = "2a_variavel"
print(nome_invalido.isidentifier())

com_espaco = "variavel numero um"
print(com_espaco.isidentifier())