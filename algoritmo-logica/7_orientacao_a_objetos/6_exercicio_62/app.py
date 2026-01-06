"""
crie um sistema que simule um banco, a classe Banco deve ter um metodo de saque, deposito e transferencia
propriedades como nome do proprietario da conta e saldo
realizar saques,deposito e transferencia entre contas
"""
class Banco():
    def __init__(self, nome,saldo):
        self.nome = nome
        self.saldo = saldo

    def deposito(self,valor):
        self.saldo += valor

    def saque(self,valor):
        self.saldo -= valor

    def transferencia(self,outra_conta,valor):
        self.saldo += valor
        outra_conta.saldo += valor



conta_matheus = Banco('Matheus',1000)
print(conta_matheus.nome)

conta_matheus.deposito(1000)
print(conta_matheus.saldo)