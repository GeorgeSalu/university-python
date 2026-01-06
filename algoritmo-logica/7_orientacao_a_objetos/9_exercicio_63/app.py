"""
crie uma classe Pessoa com nome e idade
crie uma classe de Super heroi que herda as caracteristicas de pessoa
crie poderes especiais para o super heroi
test as duas classes criando novos objetos
"""
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print("ola galera")


class Superheroi(Pessoa):
    def __init__(self,nome,idade,super_podere):
        super().__init__(nome,idade)
        self.super_podere = super_podere

    def utilizar_super_pode(self):
        print("o heroi utilizou o %s"%self.super_podere)

joao = Pessoa("joao", 21)
joao.falar()

matheus = Superheroi("matheusa", 21, "raio laser")
matheus.falar()
matheus.utilizar_super_pode()