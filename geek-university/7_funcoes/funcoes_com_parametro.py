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

# Funções podem ter n parametros de entrada. ou seja,podemos receber como entrada
# numa função qquantos parametros forem necessarios, eles são separados por vírgula

# exemplos

def soma(a,b):
    return a+b

def multiplicar(a,b):
    return a*b

def outra(num1,b, msg):
    return (num1+b)*msg

print(soma(3,4))
print(soma(10,20))

# se for informado um número errado de parametros ou argumetos, teremos TypeError

# parametros nomeados

def nome_completo(nome,sobrenome):
    return f'seu nome completo eh {nome} {sobrenome}'


print(nome_completo('angeline','jolie'))

