#!/usr/local/bin/python3
# conceito          nota
# A                 de 10.0 a 9.1
# A-                de 9.0 a 8.1
# B                 de 8.0 a 7.1
# B-                de 7.0 a 6.1
# C                 de 6.0 a 5.1
# C-                de 5.0 a 4.1
# D                 de 4.0 a 3.1
# D-                de 3.0 a 2.1
# E                 de 2.0 a 1.1
# E-                de 1.0 a 0.0

def nota_conceito(valor):
    nota = float(valor)

    if nota > 10:
        return 'Nota inválida'
    elif nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A-'
    elif nota >= 7.1:
        return 'B'
    elif nota >= 6.1:
        return 'B-'
    elif nota >= 5.1:
        return 'C'
    elif nota >= 4.1:
        return 'C-'
    elif nota >= 3.1:
        return 'D'
    elif nota >= 2.1:
        return 'D-'
    elif nota >= 1.1:
        return 'E'
    elif nota >= 0:
        return 'E-'
    else:
        return 'Nota inválida'


if __name__ == '__main__':
    valor_informado = input('Nota do aluno: ')
    conceito = nota_conceito(valor_informado)
    print(conceito)