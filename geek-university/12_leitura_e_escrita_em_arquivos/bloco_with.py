"""
o bloco with

Passo para se trabalhar com arquivos

# 1 - abrimos o arquivo
# 2 - manipulamos o arquivo
# 3 - fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados
são fechados após o bloco with

arquivo = open('texto.txt')
"""

with open('texto.txt', 'w') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)