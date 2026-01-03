"""
crie uma funcao que retorna se um numero é maior ou menor que 10
o numero deve ser passado como parâmetro
"""
a = 10
b = 9
c = 16

def maior_que_dez(num):
    resultado = ""
    if num > 10:
        resultado = "maior que 10"
    elif num < 10:
        resultado = "menor que 10"
    else:
        resultado = "igual a 10"

    return resultado

res_um = maior_que_dez(a)
print(res_um)

res_dois = maior_que_dez(b)
print(res_dois)

res_tres = maior_que_dez(c)
print(res_tres)