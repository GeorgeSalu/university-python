# isnumeric() = verifica se todos os caracteres de uma string são numéricos, retornando True (verdadeiro) ou False (falso)
# Ele reconhece desde dígitos decimais comuns até caracteres especiais de contagem (como frações e subscritos Unicode)

codigo = "1054"
print(codigo.isnumeric())

placa = "ABC-1234"
print(placa.isnumeric())

fracao = "½"
print(fracao.isnumeric())