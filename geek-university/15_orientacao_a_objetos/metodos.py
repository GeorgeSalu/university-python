"""
POO - Metodos
- Metodos (funções) -> Representam os comportamentos do objeto,Ou seja,as ações
que este objeto pode realizar no seu sistema

Em Python,dividimos os metodos, em 2 grupos: metodos de instância e metodos de
classe

# metodo de instância
# o metodo dunder init __init__ é um metodo especial chamado de construtor e
a sua função e construir o objeto a partir da classe

obs: todo elemento em python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)
obs: os metodos/funções dunder em python são chamados de metodos magicos
ATENÇÃO! por mais que possamos criar nossas proprias funções utilizando dunder (underline
no inicio e no fim) não é aconselhado. python possui varios metodos com esta forma de nomeclatura
e pode ser que mudemos o comportamento dessas funções magicas da linguagem, então evite ao maximo
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

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

