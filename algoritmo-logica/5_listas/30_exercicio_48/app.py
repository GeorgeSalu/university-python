"""
crie um dicionario com livros que voce gosta e o numero de paginas
imprima estes valores no terminal
"""
livros = {
    "eragon": 400,
    "senhor dos aneis": 360,
    "narnia": 600
}

for livro in livros:
    print("O livro %s tem %d paginas" % (livro, livros[livro]))