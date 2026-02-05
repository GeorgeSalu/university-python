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

em python, por conveção, ficou estabelecido que, todo atributo de uma classe é publico
ou seja, pode er acessado em todo o projeto
caso queiramos demostrar que determinado atributo deve ser tratado como provado, ou seja
que deve ser acessado/utilizado somente dentro da propria classe onde está declarado, utiliza-se
__ duplo underscore no inicio de seu nome, isso é conhecido também como Name Mangling
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

# atributos publicos e atributos privados
class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostrar_senha(self):
        print(self.__senha)

    def mostrar_email(self):
        print(self.email)

# obs: lembre-se que isso é apenas uma convenção, ou seja,a linguagem python não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe

# exemplo

user = Acesso('teste@gmail.com', '12323')
print(user.email)
# print(user.__senha) AttributeError
#print(user._Acesso__senha) # temos acesso, mas não deveriamos fazer esse acesso (Name Mangling)
user.mostrar_senha()
user.mostrar_email()

# o que significa atributos de instancias ?

# significa que ao criarmos instancias/objetos de uma classe, todas as instâncias teram estes
# atributos