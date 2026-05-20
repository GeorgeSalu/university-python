# Exercício 1
# Escreva uma rotina que crie uma borda ao redor de uma palavra para destacá-la como sendo um título
# A rotina deve receber como parametro a palavra a ser destacada
# o tamanho da caixa de texto devera ser adaptável conforme o tamanho da palavra
# a seguir veja alguns exemplos de como deve ficar a borda na palavra
#
#   *-----------*
#   |    Ola    |
#   +-----------+

def borda(s1):
    tam = len(s1)
    if tam:
        print('+','-'*tam,'+')
        print('|',s1,"|")
        print('+','-'*tam,'+')


borda('Ola, Mundo')
borda('Curso de python')