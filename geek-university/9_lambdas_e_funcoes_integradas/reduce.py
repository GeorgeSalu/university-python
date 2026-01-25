"""
Reduce

obs: apartir do python3+ a função reduce() não é mais uma função integrada (built-in). Agora temos
que importar e utilizar esta função a partir do módulo 'functools'

Guido Van Rossum: Utilize a função reduce() se você realmente precisa dela. em todo caso 99%
das vezes um loop for é mais legível

Para entender o reduce()

# imagine que voce tem uma coleção de dados:
dados = [a1,a2,a3,a4,....an]
# e voce tem uma função que recebe dois parametros
def funcao(x, y):
    return x + y)

assim como map() e filter(), a função reduce() recebe dois parametros: a função e o iteravel
reduce(funcao, dados)
A funcao reduce(), funciona da seguinte forma:
- passo 1: res1 = f(a1,a2) # aplica a função nos dois primeiros elementos da colecaçõ e guarda o resultado
- passo 2: res2 = f(res1, a3) # aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o res
  Isso é repetido ate o fimnal.
  passo 3: res3 = f(res2, a4)
  .
  .
  .
  passo n: resn = f(resm, an)
ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. no final
reduce() irá retornar o resultado final

alternativamente, poderiamos ver a função reduce() como:
funcao(funcao(funcao(a1, a2), a3), a4), ...), an)
"""