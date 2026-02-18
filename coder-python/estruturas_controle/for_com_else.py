PALAVRAS_PROIBIDAS = ('futebol','religiao','politica')
textos = [
    'joao gosta de futebol e politica',
    'a praia foi divertida'
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('o texto possui pelo menos uma palavra proibida', palavra)
            break
    else:
        print('texto autorizado', texto)