"""
Reduce

obs: apartir do python3+ a função reduce() não é mais uma função integrada (built-in). Agora temos
que importar e utilizar esta função a partir do módulo 'functools'

Guido Van Rossum: Utilize a função reduce() se você realmente precisa dela. em todo caso 99%
das vezes um loop for é mais legível

Para entender o reduce()

# imagine que voce tem uma coleção de dados:
dados = [a1,a2,a3,a4,....an]
# e voce tem uma função que recebe dois parâmetros
def funcao(x, y):
    return x + y)

assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável
reduce(funcao, dados)
A funcao reduce(), funciona da seguinte forma:
- passo 1: res1 = f(a1,a2) # aplica a função nos dois primeiros elementos da coleção e guarda o resultado
- passo 2: res2 = f(res1, a3) # aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o res
  Isso é repetido ate o final.
  passo 3: res3 = f(res2, a4)
  .
  .
  .
  passo n: resn = f(resm, an)
ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. no final
reduce() irá retornar o resultado final

alternativamente, poderíamos ver a função reduce() como:
funcao(funcao(funcao(a1, a2), a3), a4), ...), an)
"""

# como funciona na prática ?
# vamos utilizar a função reduce() para multiplicar todos os números de uma lista
from functools import reduce

dados = [2,3,4,5,7,11,13,17,19,23,29]

# pra utilizar o reduce() nos precisamos de uma função que receba dois parametros
multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# utilizando um loop normal
res = 1
for n in dados:
    res = res * n

print(res)