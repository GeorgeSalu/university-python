palavra = input("digite uma palavra secreta: ").lower().strip()

for x in range(50):
    print()

digitadas = []
acertos = []
erros = 0

while True:
    adivinha = ""
    for letra in palavra:
        if letra in acertos:
            adivinha += letra
        else:
            adivinha += "\u2588"
    print(f"adivinhe ({len(palavra)} letras) : ")
    for letra in adivinha:
        print(f"{letra}", end="")
    print()

    # condição de vitoria
    if adivinha == palavra:
        print("voce acertou")
        break

    # tentativas
    tentativa = input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("voce ja usou essa latra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print(f"voce errou")