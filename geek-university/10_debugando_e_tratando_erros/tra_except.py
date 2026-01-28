"""
O block tray/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso codigo, previnindo
assim que o programa pare de funcionar e o usuario receba mensagens de erro inesperadas

A forma geral mais simples é:

try:
    // execução problematica
except
    // o que deve ser feito em caso de problema
"""
# exemplo 1 - tratando um erro generico

try:
    geek()
except:
    print('Ocorreu um erro')
