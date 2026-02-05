"""
POO - atributos

Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos
conseguimo-nos representar computacionalmente os estados de um objeto

Em python, dividimos os atributos em 3 grupos:
    - atributos de instância
    - atributos de classe
    - atributos dinamicos

# atributos de instância: são atributos declarados dentro do metodo construtor
# obs: metodo contrutor: é um metodo especial utilizado para construção do objeto
"""
class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
