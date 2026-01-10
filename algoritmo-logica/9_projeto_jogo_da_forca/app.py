from palavras import palavras
import random

# seleciona palavra
def selecionar_palavra():
    palavra = random.choice(palavras)
    return palavra.upper()

# iniciar o jogo
def jogar(palavra):
    # defininco variaveis
    palavra_a_completar = "_"*len(palavra)
    advinhou = False
    letras_utilizadas = []
    palavras_utilizadas = []
    tentativas = 6

    print(palavra)
    print(palavra_a_completar)

    # boas vindas ao jogador
    print("vamos jogar")
    print(exibir_forca(tentativas))
    print("esta é a palavra: %s"%palavra_a_completar)


# status do jogo
def exibir_forca(tentativas):
    estagios = [  # Fim de jogo
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
        """,
        # Falta 1 tentativa
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / 
            -
        """,
        # Faltam 2 tentativas
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |      
            -
        """,
        # Faltam 3 tentativas
        """
            --------
            |      |
            |      O
            |     \\|
            |      |
            |     
            -
        """,
        # Faltam 4 tentativas
        """
            --------
            |      |
            |      O
            |      |
            |      |
            |     
            -
        """,
        # Faltam 5 tentativas
        """
            --------
            |      |
            |      O
            |    
            |      
            |     
            -
        """,
        # Estado inicial
        """
            --------
            |      |
            |      
            |    
            |      
            |     
            -
        """
    ]

    return estagios[tentativas]

# iniciaçõ do jogo e continuar jogando
def iniciar():
    palavra = selecionar_palavra()
    jogar(palavra)

iniciar()