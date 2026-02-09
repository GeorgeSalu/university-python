"""
POO - Objetos

Objetos -> São instancias de classe,Ou seja,após o mapeamento do objeto do mundo real para a sua
represetação computacional, devemos poder criar quantos objetos forem necessarios, podemos pensar
nos objetos/instancias de uma classe como variaveis do tipo definido na classe
"""
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