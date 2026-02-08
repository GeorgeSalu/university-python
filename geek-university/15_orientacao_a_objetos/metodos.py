"""
POO - Metodos
- Metodos (funções) -> Representam os comportamentos do objeto,Ou seja,as ações
que este objeto pode realizar no seu sistema

Em Python,dividimos os metodos, em 2 grupos: metodos de instância e metodos de
classe

# metodo de instância
# o metodo dunder init __init__ é um metodo especial chamado de construtor e
a sua função e construir o objeto a partir da classe
"""
# metodos de instância
class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 1234

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    def __init__(self, nome, descricao, valor):
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha