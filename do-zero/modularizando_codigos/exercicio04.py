# Exercício 4
# Escreva uma função para validar uma string
# Essa função recebe como parametro a string, o número minimo e máximo de caracteres
# retorne verdadeiro se o tamanho da string estiver entre os valores minimo e máximo, e falso caso contrario

def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while (tam < min) or (tam > max):
        s1 = input(pergunta)
        tam = len(s1)
    return s1


# programa principal
x = valida_string('digite uma string', 10,30)
print(f"voce digitou a string: {x}. dado valido. encerrando")