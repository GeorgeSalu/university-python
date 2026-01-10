from palavras import palavras
import random

# seleciona palavra
def selecionar_palavra():
    palavra = random.choice(palavras)
    return palavra.upper()

teste = selecionar_palavra()
print(teste)