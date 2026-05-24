def verificar_idade(idade):
    if idade < 18:
        return 'menor de idade'
    else:
        return 'maior de idade'

# programa principal
print(verificar_idade(int(input('digite idade : '))))