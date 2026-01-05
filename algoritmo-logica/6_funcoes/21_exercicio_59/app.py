import random

aleatorio = random.randint(1,10)

papite = int(input('Digite um numero de 1 a 10: '))

if aleatorio == papite:
    print("parabens vc acertou")
else:
    print("voce errou")