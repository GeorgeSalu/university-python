def par_impar(x):
    if x % 2 == 0:
        return 'par'
    else:
        return 'impar'


# programa principal
print(par_impar(int(input('digite um valor inteiro : '))))