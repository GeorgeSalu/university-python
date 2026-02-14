# tabela verdade do AND
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# tabela verdade do OR
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# operador de negação
print(not True)
print(not False)

# desafio operadores logicos
trabalho_terca = False
trabalho_quinta = False

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete

print("tv50={} tv32={} sorvete={} saudavel={}".format(tv_50, tv_32, sorvete, mais_saudavel))