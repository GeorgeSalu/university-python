class Pessoa:
    def __init__(self, nome, idade,profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

matheus = Pessoa("Matheus", 20, "programador")
print(matheus.__str__())