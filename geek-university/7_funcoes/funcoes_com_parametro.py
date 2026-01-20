"""
Funcoes com parametros (de entrada)
- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar num programa qualquer, geralmente temos:
entrada -> processamento -> saida

Se a gente pensar numa função,ja sabemos que temos funções que:
- não possuem entrada
- não possuem saida
- possuem entrada, mas nãp possuem saida
- não possuem entrada m possuem saidaa
- possuem entrada e saida
"""
def quadrado(numero):
    return numero ** 2

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)