"""
Seek e Cursors

seek() -> é utilizado para movimentar o cursos pelo arquivo
"""
arquivo = open('texto.txt')
print(arquivo.read())

# seek() -> a função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe um
# parametro que indica onde queremos colocar o cursor.

# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0)

print(arquivo.read())

# readline() -> função que le o arquivo linha a linha
print(arquivo.readline())