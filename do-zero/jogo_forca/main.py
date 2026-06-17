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
    print(f"adivinhe: ")
    for letra in adivinha:
        print(f"{letra}", end="")

    break