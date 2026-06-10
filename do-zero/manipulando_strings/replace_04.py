# replace() = substitui caracteres por outros
dados = "12/05/2026"
# Como replace() retorna uma string, você pode encadear vários métodos na mesma linha.
formatado = dados.replace("/", "-").replace("12", "15")
print(formatado)