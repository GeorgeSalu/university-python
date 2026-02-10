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

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class ContaCorrente:

    contador = 1234

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha


# instancia/objetos
lamp1 = Lampada('branca',110, 60)
lamp1.ligar_desligar()
print(f'A lampada esta ligada ? {lamp1.checa_lampada()}')

cc1 = ContaCorrente(5000, 2000)
user1 = Usuario('felicity','jones','felicity@gmail.com','1234555')

