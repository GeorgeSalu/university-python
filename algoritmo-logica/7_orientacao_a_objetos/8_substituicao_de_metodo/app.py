class Pessoa:
    def falar(self):
        print("ola pessoal")

class Matheus(Pessoa):
    def falar(self):
        print("ola pessoal, eu sou o matheus")

matheus = Matheus()
matheus.falar()