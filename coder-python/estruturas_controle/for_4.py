# Função sortear_dado numeros entre 1 e 6
# for com range 1 a 6
# se for impar continue
# se numero for par e igual ao valor sorteado pela função dado
# imprimir 'ACERTOU' e depois chamar o break
# se não acertar chamar o else.... print('Nao acertou o numero')
from random import randint

def sortear_dado():
    return randint(1,6)

for i in range(1,7):
    if i % 2 == 1:
        continue

    if sortear_dado() == i:
        print('ACERTOU', i)
        break
else:
    print('nao acertou o numero')