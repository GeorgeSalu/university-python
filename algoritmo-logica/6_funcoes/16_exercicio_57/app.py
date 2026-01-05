"""
crie uma funcao que recebe uma sequencia de parametros numericos
multiplique todos eles e exiba o valor no terminal
"""
def multiplica_numeros(*numeros):
    resultado = 1
    for num in numeros:
        resultado = resultado * num

    return resultado

print(multiplica_numeros(1,2,3,4,5))
res = multiplica_numeros(5,4,2,1)
print(res)
