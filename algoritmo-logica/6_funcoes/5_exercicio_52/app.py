"""
escreva uma funcao que recebe um dado em texto
se esse dado tem mais que 20 caracteres, retorne que é um texto longo
se tem menos, retorne que é um texto curto
"""
def checa_tamanho_texto(texto):
    resposta = ""
    if len(texto) > 20:
        resposta = "texto muito longo"
    else:
        resposta = "texto curto"

    return resposta

texto_um = "o matheus é programador"
resposta = checa_tamanho_texto(texto_um)
print(resposta)
print(len(texto_um))