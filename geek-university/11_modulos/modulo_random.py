"""
Modulo Random e o que são modulos?

- Em Python, modulos nada mais são do que outros arquivos Pyhon

Modulo Random -> Possui variaveis funções para geração de números pseudoaleatorio
"""
# obs: existem duas formas de se utilizar um módulo ou função deste
# domra 1 - importando todo o modulo (não remocomendado)
import random

# random() -> gera um real numero pseudoaleatorio enre 0 e 1

# obs: ao realizar o import de todo o modulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do modulo ficarãp disponiveis (ficarão na memoria). caso você saiba quais funções voce precisa utilizar
# deste modulo, então esta seria a forma ideial de utilização. nos veremos uma forma melhor na Forma 2

print(random.random())

# veja que para utilizar a função random() do pacote random, nos colocamos o nome do pacote e o nome da função
# separados por ponto

# obs: não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é apenas
# uma função dentro do módulo random

# forma 2 - importando uma função específica do módulo (forma recomendada)

from random import random

# no import acima, estamos falando: do módulo random, importe a função random

for i in range(10):
    print(random())

# uniforma() -> gerar um numero real pseudoaletorio entre os valores estabelicidos

from random import uniform

for i in range(10):
    print(uniform(3, 7)) # 7 não é incluido

# randint() -> gera valores pseudoaleatorios entre os valores estabelecidos
from random import randint

# gerador de apostas para mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')


# choice() -> mostra um valor aleatorio entre um iteravel

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))