"""
Erros mais comuns em python

Atenção! É importante prestar atenção e aprender a ler as saidas de erros geradas pela execução
do nosso codigo

Os erros mais comuns:
1 - SyntaxError -> ocorre quando o python encontra um erro de sintaxe. ou seja, você escreveu algo que o
python não reconhece como parte da linguagem

exemplos SyntaxError:
a)
    def funcao:
        print('geek')
b)
    def = 1
c)
    return

2 - NameError -> Ocorre quando uma variavel ou função não foi definindo

exemplos NameError:
a)
    print(geek)
b)
    geek()

3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errdo

exemplos TypeError:
a)
    print(len(5))

b)
    print('geek'+[])

4 - IndexError -> ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
um indice invalido

exemplos IndexError:

a)
    lista = ['geek']
    print(lista[2])
b)
    lista = ['geek']
    print(lista[0][10])
c)
    tupla = ('geek')
    print(tupla[0][10])

5 - ValueError -> ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto, mas valor inapropriado

exemplos ValueError:
a)
    print(int('geek'))

6 - KeyError -> ocorre quando tentamos acessar um dicionario com uma chave que não existe

exemplos KeyError:

a)
    dic = {'python':'university'}
    print(dic['geek'])

7 - AttributeError -> Ocorre quando uma variavel não tem um atributo/função

exemplos AttributeError:
a)
    tupla = (1, 2, 3)
    print(tupla.sort())

8 -> IndenttionError -> Ocorre quando não respeitamos a indentação do python

exemplos IndenttionError:
a)
def nova():
print('geek')

obs: Exceptions e Erros são sinonimos na programação
obs: Importante ler e prestar atenção na saida de erro
"""