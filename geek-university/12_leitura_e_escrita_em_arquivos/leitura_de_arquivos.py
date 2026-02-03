"""
Leitura de arquivos

Para ler o conteudo de um arquivo em python, utilizamos a função integrada open()
que literalmente significa 'abrir'

open() -> na forma mais simples de utilização nos passamos apenas um parametro de
entrada, que neste caso é o nome do arquivo a ser lido. Essa função retorna um
_io.TextIoWrapper e é com ele que trabalhamos então

obs:  por padrão, a função open() abre o arquivo para leitura, este arquivo deve
existir, ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>

mode r -> modo de leitura. r -> read() -> ler
"""
# exemplo
arquivo = open('texto.txt')

# print(arquivo)
# print(type(arquivo))

# para ler o conteudo de um arquivo, após a sua abertura, devemos utilizar a função read()
print(arquivo.read())

# obs: o python, utiliza um recurso para trabalhar com arquivo chamado cursor. Esse cursor,
# funciona como o cursor quando estamos escrevendo 